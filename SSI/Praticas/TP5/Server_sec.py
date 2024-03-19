import asyncio
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

#Numero de coneccoes
conn_cnt = 0

#Porta de coneccao
conn_port = 8443

#Tamanho maximo das mensagens
max_msg_size = 9999

class ServerWorker(object):
    def __init__(self, cnt, addr=None):
        #contador
        self.id = cnt

        #endereco
        self.addr = addr

        #Contador de mensagens
        self.msg_cnt = 0

        #chave de criptografia
        self.key = b'your_secret_password173200172018' [:32]

    def process(self, msg):
        #Incrementa o numero de mensagens recebidas
        self.msg_cnt += 1 

        #Imprime a mensagem decriptografada
        txt = self._decrypt_message(msg)
        print('%d : %r' % (self.id,txt.decode()))

        #Encripta a mensagem em caixa alta
        new_msg = self._encrypt_message(txt.upper())
        return new_msg if len(new_msg)>0 else None
    
    def _encrypt_message(self, plaintext):
        chacha = AESGCM(self.key)
        nonce = os.urandom(12)
        return nonce + chacha.encrypt(nonce, plaintext, None)

    def _decrypt_message(self, ciphertext):
        chacha = AESGCM(self.key)
        nonce = ciphertext[:12]
        decrypted_data = chacha.decrypt(nonce, ciphertext[12:], None)
        return decrypted_data


async def handle_echo(reader, writer):
    global conn_cnt

    #Incrementa o numero de coneccoes
    conn_cnt +=1

    #Obtem o endereco do cliente
    addr = writer.get_extra_info('peername')

    #Cria uma instancia do ServerWorker
    srvwrk = ServerWorker(conn_cnt, addr)

    #Le os dados recebidos e processaos ate que nao haja mais dados
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
    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    print('  (type ^C to finish)\n')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    print('\nFINISHED!')

run_server()