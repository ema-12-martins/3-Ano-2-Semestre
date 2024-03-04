import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

def attack(cipher_text_file_path,position,position_cipher_text,plaintext):
    with open(cipher_text_file_path,'rb') as cipher_text_file:
        nonce=cipher_text_file.read(16)
        cipher_text=cipher_text_file.read()

    


    with open(f"{cipher_text_file_path}.dec",'wb') as plaintext_file:
        plaintext_file.write(plaintext)


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


