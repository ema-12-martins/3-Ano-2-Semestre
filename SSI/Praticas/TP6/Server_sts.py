import asyncio
import os
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import myCrypt as mc
from cryptography import x509
import random

conn_cnt = 0
conn_port = 8442
max_msg_size = 9999

class ServerWorker(object):
    def __init__(self, cnt, addr=None):
        self.id = cnt
        self.addr = addr
        self.msg_cnt = 0

        #generates a base^exp number, where exp is random
        self.base = 2
        self.exp = random.randint(2, 10) 
        self.gy = self.base**self.exp
        
        with open('MSG_SERVER.key','rb') as key_file:
            self.serverRSA_private_key = serialization.load_pem_private_key(key_file.read(),password=b"1234")

        self.serverRSA_public_key = self.serverRSA_private_key.public_key()

        self.certificate=mc.cert_load('MSG_SERVER.crt')
        self.ca_certificate=mc.cert_load('MSG_CA.crt')


    def process(self, msg):
        if self.msg_cnt < 2:
            return self._process_handshake(msg)
        else:
            return self._process_message(msg)


    def _process_handshake(self, msg):
        if self.msg_cnt==0:
            self.peerRSA_public_key = load_pem_public_key(mc.unpair(msg)[0])
            self.peerGX = int.from_bytes(mc.unpair(msg)[1],'big')
            self.shared_key = self.peerGX**self.exp

            self.aesgcm = AESGCM(HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'handshake data',
                backend=default_backend()
            ).derive(self.shared_key.to_bytes(1000, 'big')))

            #Server Signature
            serverSignature = self.serverRSA_private_key.sign(
                mc.mkpair(self.gy.to_bytes(1000, 'big'),self.peerGX.to_bytes(1000, 'big')),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            nonce = os.urandom(12) 
            ct = nonce + self.aesgcm.encrypt(nonce, serverSignature, None)
            
            self.msg_cnt += 1

            return mc.mkpair(mc.mkpair(mc.mkpair(self.serverRSA_public_key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo),self.gy.to_bytes(1000, 'big')),ct),self.certificate.public_bytes(encoding=serialization.Encoding.PEM))
        
        elif self.msg_cnt==1:
            #Client Signature Validation
            nonce = (mc.unpair(msg)[0])[:12]
            serverEncryptedSignature = (mc.unpair(msg)[0])[12:]
            aad = b""
            serverDecryptedSignature = self.aesgcm.decrypt(nonce, serverEncryptedSignature, aad)

            # Client Certificate Validation
            client_certificate=x509.load_pem_x509_certificate(mc.unpair(msg)[1])
            mc.valida_certCliente(self.ca_certificate,client_certificate)
            
            try:
                self.peerRSA_public_key.verify(
                    serverDecryptedSignature,
                    mc.mkpair(self.peerGX.to_bytes(1000, 'big'),self.gy.to_bytes(1000, 'big')),
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
            except InvalidSignature:
                print("Validação da assinatura digital não efetuada!!!")
                return
            
            return self._process_message(None)
        

    def _process_message(self, msg):
        self.msg_cnt+=1

        if msg:
            nonce = msg[:12]
            informacao = msg[12:]
            aad = b""
            decrypted_msg = self.aesgcm.decrypt(nonce, informacao, aad)
            print('%d : %r' % (self.id,decrypted_msg.decode()))

            new_msg = decrypted_msg.upper()

            nonce = os.urandom(12)
            ct = nonce + self.aesgcm.encrypt(nonce, new_msg, aad)
            return ct if len(new_msg) > 0 else None
        
        else: ##Caso em que acontece a validacao da signature do cliente
            return b"Handshake terminado com sucesso!!!"


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