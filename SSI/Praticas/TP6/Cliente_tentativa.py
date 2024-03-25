import asyncio
import socket
import funcoes_auxiliares as fa
import secrets
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key

conn_port = 8443
max_msg_size = 9999

class Client:
    def __init__(self, sckt=None):
        self.sckt = sckt
        self.msg_cnt = 0

        with open("MSG_CLI1.key", "rb") as key_file:
            self.client_private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=b"1234") 
        
        self.client_public_key = self.client_private_key.public_key()

    def process(self, msg=b""):
        if self.msg_cnt == 0:
            self.msg_cnt +=1
            return self.client_public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
        
        self.msg_cnt+=1
        print('Received (%d): %r' % (self.msg_cnt , msg.decode()))
        print('Input message to send (empty to finish)')
        new_msg = input().encode()
        return new_msg if len(new_msg)>0 else None


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
