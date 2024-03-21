# Código baseado em https://docs.python.org/3.6/library/asyncio-stream.html#tcp-echo-client-using-streams
import asyncio
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
import funcoes_auxiliares as fa
from cryptography.hazmat.primitives.asymmetric import padding
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
        
        with open("MSG_SERVER.key", "rb") as key_file:
            self.server_private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=b"1234",
        ) 
        self.server_public_key = self.server_private_key.public_key()


    def process(self, msg):
        if self.msg_cnt == 0:
            print(msg)
            
            try:
                self.peer_public_key = load_der_public_key(msg)
                self.shared_key = self.server_private_key.exchange(self.peer_public_key)
            except Exception as e:
                print("Error loading DER public key:", e)
            self.derived_key = HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=b'handshake data',
            ).derive(self.shared_key)
            self.aesgcm = AESGCM(self.derived_key)

            client_PublicKey = msg

            signature = self.server_private_key.sign(
                fa.mkpair(self.server_public_key, client_PublicKey),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )           
            
            send = fa.mkpair(self.server_public_key, signature)
            self.msg_cnt += 1
            return send, self.msg_cnt

        self.msg_cnt += 1
        nonce = msg[:12]
        informacao = msg[12:]
        aad = b""
        msg = self.aesgcm.decrypt(nonce, informacao, b"")
   
        new_msg = msg.upper()
        print("new msg: ", new_msg.decode())

        nonce = os.urandom(12)

        ct = nonce + self.aesgcm.encrypt(nonce, new_msg, aad)
    
        return ct,self.msg_cnt if len(new_msg)>0 else None,self.msg_cnt


async def handle_echo(reader, writer):
    global conn_cnt
    conn_cnt +=1
    addr = writer.get_extra_info('peername')
    srvwrk = ServerWorker(conn_cnt, addr)
    data = await reader.read(max_msg_size)
    while True:
        if not data: continue
        if data[:1]==b'\n': break
        data,msg_cnt = srvwrk.process(data)
        if (not data) and msg_cnt>2: break
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