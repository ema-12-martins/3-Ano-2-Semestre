import asyncio
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

#Define a porta a que o cliente se tentara ligar
conn_port = 8443

#Tamanho maximo que o cliente esta dispsoto  a receber
max_msg_size = 9999

class Client:
    def __init__(self, sckt=None):
        #socket
        self.sckt = sckt

        #contador de mensagens
        self.msg_cnt = 0

        #Define uma chave a ser usada, com 32 bytes
        self.key = b'your_secret_password173200172018' [:32]

    def process(self, msg=b""):

        #Verifica se temos mensagens recebidas. Imprime a mensagem recebida se esta existir.
        if self.msg_cnt!=0:
            print('Received (%d): %r' % (self.msg_cnt , self._decrypt_message(msg).decode()))

        #Incrementa contador de mensagens
        self.msg_cnt +=1

        #Solicita que insira uma mensagem para mandar para o servidor
        print('Input message to send (empty to finish)')
        #Le do terminal, passa para bytes e encripta a menssagem.
        new_msg = self._encrypt_message(input().encode())
        #Retorna a mensagem criptografada, a menos qie seja nula
        return new_msg if len(new_msg)>0 else None

    def _encrypt_message(self, plaintext):
        #Inicia o objeto com a chave criptografada
        chacha = AESGCM(self.key)
        #Cria o nonce
        nonce = os.urandom(12)
        #Retorna o nonce mais a mensagem criptografada
        return nonce + chacha.encrypt(nonce, plaintext, None)

    def _decrypt_message(self, ciphertext):
        #Inicia o objeto com a chave criptografada
        chacha = AESGCM(self.key)
        #Extrai o nonce do inicio da mensagem criptografada
        nonce = ciphertext[:12]
        #Decripta os dados
        decrypted_data = chacha.decrypt(nonce, ciphertext[12:], None)
        return decrypted_data


async def tcp_echo_client():
    #Abre uma coneccao TCP em 127.0.0.1
    reader, writer = await asyncio.open_connection('127.0.0.1', conn_port)

    #Obter o par endereco-porta
    addr = writer.get_extra_info('peername')

    #Cria uma instancia cliente com o endereco do par.
    client = Client(addr)

    #Processa a primeira mensagem
    msg = client.process()
    #Enquanto tiver mensagens para processar
    while msg:
        #Escreve a mensagem
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
    #Loop de eventos assincronos
    loop = asyncio.get_event_loop()
    #Executa o TCP assincrono ate que seja concluido
    loop.run_until_complete(tcp_echo_client())


run_client()