# Código baseado em https://docs.python.org/3.6/library/asyncio-stream.html#tcp-echo-client-using-streams
import asyncio
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.asymmetric import dh

from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_der_public_key

conn_cnt = 0
conn_port = 8442
max_msg_size = 9999
class ServerWorker(object):
    def __init__(self, cnt, addr=None):
        self.id = cnt
        self.addr = addr
        self.msg_cnt = 0
        p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
        g = 2
        pn = dh.DHParameterNumbers(p, g)
        parameters = pn.parameters()
        self.server_private_key = parameters.generate_private_key()
        self.server_public_key = self.server_private_key.public_key()
        self.aesgcm = None

    def process(self, msg):
        if self.msg_cnt == 0:
            return self._process_handshake(msg)
        else:
            return self._process_message(msg)

    def _process_handshake(self, msg):
        self.peer_public_key = load_der_public_key(msg)
        self.shared_key = self.server_private_key.exchange(self.peer_public_key)
        self.derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
        ).derive(self.shared_key)
        self.aesgcm = AESGCM(self.derived_key)
        self.msg_cnt += 1
        return self.server_public_key.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)

    def _process_message(self, msg):
        
        if msg:
            nonce = msg[:12]
            informacao = msg[12:]
            aad = b""
            decrypted_msg = self.aesgcm.decrypt(nonce, informacao, aad)
            print("Decrypted message:", decrypted_msg.decode())

        # Change behavior of the server here
        new_msg = decrypted_msg.upper()
        print("new msg: ", new_msg.decode())

        nonce = os.urandom(12)
        ct = nonce + self.aesgcm.encrypt(nonce, new_msg.encode(), aad)
        return ct if len(new_msg) > 0 else None


async def handle_echo(reader, writer):
    global conn_cnt
    conn_cnt +=1
    addr = writer.get_extra_info('peername')
    srvwrk = ServerWorker(conn_cnt, addr)
    data = await reader.read(max_msg_size)
    while True:
        if not data: continue
        if data[:1]==b'\n': break
        data = srvwrk.process(data)
        if not data: break
        writer.write(data)
        await writer.drain()
        data = await reader.read(max_msg_size)
    print("[%d]" % srvwrk.id)
    writer.close()


def run_server():
    loop = asyncio.new_event_loop()
    coro = asyncio.start_server(handle_echo, '127.0.0.1', conn_port)
    server = loop.run_until_complete(coro)
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    print('  (type ^C to finish)\n')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    print('\nFINISHED!')

run_server()