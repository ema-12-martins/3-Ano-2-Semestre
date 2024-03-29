import asyncio
import secrets
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

conn_port = 8442
max_msg_size = 9999

class Client:
    def __init__(self, sckt=None):
        self.sckt = sckt
        self.msg_cnt = 0
                
        #generates a base^exp number, where exp is random
        self.base = 2
        self.exp = random.randint(2, 10) 
        self.gx = self.base**self.exp

        with open('MSG_CLI1.key','rb') as key_file:
            self.clientRSA_private_key = serialization.load_pem_private_key(key_file.read(),password=b"1234")
        
        self.clientRSA_public_key = self.clientRSA_private_key.public_key()

        self.client_certificate=mc.cert_load('MSG_CLI1.crt')
        self.ca_certificate=mc.cert_load('MSG_CA.crt')

        
    def process(self, msg=b""):
        if self.msg_cnt < 2:
            return self._process_handshake(msg)
        else:
            return self._process_message(msg)


    def _process_handshake(self, msg=b""):
        if self.msg_cnt==0:
            self.msg_cnt+=1
            return mc.mkpair(self.clientRSA_public_key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo),self.gx.to_bytes(1000, 'big'))
        
        elif self.msg_cnt==1:
            self.peerRSA_public_key = load_pem_public_key(mc.unpair(mc.unpair(mc.unpair(msg)[0])[0])[0])
            gy = int.from_bytes(mc.unpair(mc.unpair(mc.unpair(msg)[0])[0])[1],'big')
            self.shared_key = gy**self.exp

            self.aesgcm = AESGCM(HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'handshake data',
                backend=default_backend()
            ).derive(self.shared_key.to_bytes(1000, 'big')))

            # Server Certificate Validation
            server_certificate=x509.load_pem_x509_certificate(mc.unpair(msg)[1])
            mc.valida_certServidor(self.ca_certificate,server_certificate)

            #Server Signature Validation
            nonce = mc.unpair(mc.unpair(msg)[0])[1][:12]
            serverEncryptedSignature = mc.unpair(mc.unpair(msg)[0])[1][12:]
            aad = b""
            serverDecryptedSignature = self.aesgcm.decrypt(nonce, serverEncryptedSignature, aad)

            try:
                self.peerRSA_public_key.verify(
                    serverDecryptedSignature,
                    mc.mkpair(gy.to_bytes(1000, 'big'),self.gx.to_bytes(1000, 'big')),
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
            except InvalidSignature:
                print("Validação da assinatura digital não efetuada!!!")
                return

            #Client Signature
            clientSignature = self.clientRSA_private_key.sign(
                mc.mkpair(self.gx.to_bytes(1000, 'big'),gy.to_bytes(1000, 'big')),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
   
            nonce = os.urandom(12) 
            ct = nonce + self.aesgcm.encrypt(nonce, clientSignature, None)
            
            self.msg_cnt+=1
            return mc.mkpair(ct,self.client_certificate.public_bytes(encoding=serialization.Encoding.PEM))


    def _process_message(self, msg):
        if self.msg_cnt==2:
            print(msg.decode())

        elif self.msg_cnt>2:
            nonce = msg[:12]
            informacao = msg[12:]
            aad = b""
            decrypted_msg = self.aesgcm.decrypt(nonce, informacao, aad)
            print("Decrypted message:", decrypted_msg.decode())

        print('\nInput message to send (empty to finish)')
        new_msg = input(">> ")
        if new_msg:
            self.msg_cnt +=1
            nonce = secrets.token_bytes(12)
            ct = nonce + self.aesgcm.encrypt(nonce, new_msg.encode(), b"")
            return ct if len(new_msg) > 0 else None
                

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