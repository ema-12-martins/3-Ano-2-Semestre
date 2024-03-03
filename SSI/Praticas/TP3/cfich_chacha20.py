import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

def generateKey(key_path):
    key = os.urandom(32)
    with open(key_path,'wb+') as key_file:
        key_file.write(key)

def encrypt(plaintext_file_path,key_file_path):
    with open(key_file_path,'rb') as key_file:
        key=key_file.read()
    with open(plaintext_file_path,'rb') as plaintext_file:
        plaintext=plaintext_file.read()
    
    nonce=os.urandom(16)

    cipher = Cipher(algorithms.ChaCha20(key,nonce), mode=None)
    encryptor = cipher.encryptor()
    cipher_message = encryptor.update(plaintext)

    with open(f'{plaintext_file_path}.enc','wb+') as encoded_file:
        encoded_file.write(nonce)
        encoded_file.write(cipher_message)

def decrypt(encoded_file_path,key_file_path):
    with open(key_file_path,'rb') as key_file:
        key=key_file.read()
    with open(encoded_file_path,'rb') as encoded_file:
        nonce= encoded_file.read(16)
        cipher_message=encoded_file.read()
    
    cipher = Cipher(algorithms.ChaCha20(key,nonce), mode=None)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(cipher_message)

    with open(f"{encoded_file_path}.dec",'wb') as decoded_file:
        decoded_file.write(plaintext)

def main():
    try:
        if sys.argv[1]=='setup':
            generateKey(sys.argv[2])
        elif sys.argv[1]=='enc':
            encrypt(sys.argv[2],sys.argv[3])
        elif sys.argv[1]=='dec':
            decrypt(sys.argv[2],sys.argv[3])
    except:
        print("Some error ocorred")

if __name__ == "__main__":
    main()


