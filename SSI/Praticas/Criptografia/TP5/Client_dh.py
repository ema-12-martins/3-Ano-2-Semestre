import asyncio
import secrets
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_der_public_key

conn_port = 8442
max_msg_size = 9999
class Client:
    def __init__(self, sckt=None):
        self.sckt = sckt
        self.msg_cnt = 0
        p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
        g = 2
        pn = dh.DHParameterNumbers(p, g)
        parameters = pn.parameters()
        self.client_private_key = parameters.generate_private_key()
        self.client_public_key = self.client_private_key.public_key()
        self.aesgcm = None

    def process(self, msg=b""):
        if self.msg_cnt == 0:
            return self._process_handshake(msg)
        else:
            return self._process_message(msg)

    def _process_handshake(self, msg=b""):
        if msg:
            self.peer_public_key = load_der_public_key(msg)
            self.shared_key = self.client_private_key.exchange(self.peer_public_key)

            self.derived_key = HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'handshake data',
            ).derive(self.shared_key)
            self.aesgcm = AESGCM(self.derived_key)

            return self._process_message(None)
        else:
            return self.client_public_key.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)

    def _process_message(self, msg):
        self.msg_cnt +=1
        if msg:
            nonce = msg[:12]
            informacao = msg[12:]
            aad = b""
            decrypted_msg = self.aesgcm.decrypt(nonce, informacao, aad)
            print("Decrypted message:", decrypted_msg.decode())

        print('Input message to send (empty to finish)')
        new_msg = input(">> ")
        if new_msg:
            nonce = secrets.token_bytes(12)
            ct = nonce + self.aesgcm.encrypt(nonce, new_msg.encode(), b"")
            return ct
        else:
            return None


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', conn_port)
    addr = writer.get_extra_info('peername')
    client = Client(addr)
    msg = client.process()
    while msg:
        writer.write(msg)
        msg = await reader.read(max_msg_size)
        if msg :
            msg = client.process(msg)
        else:
            break
    writer.write(b'\n')
    print('Socket closed!')
    writer.close()

def run_client():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client())


run_client()