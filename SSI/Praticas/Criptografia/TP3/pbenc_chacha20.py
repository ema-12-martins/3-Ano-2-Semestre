import sys
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

def encrypt(plaintext_file_path, key_text):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(key_text.encode())

    nonce = os.urandom(16)

    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    encryptor = cipher.encryptor()
    
    with open(plaintext_file_path, 'rb') as plaintext_file:
        plaintext = plaintext_file.read()

    cipher_message = encryptor.update(plaintext)

    with open(f'{plaintext_file_path}.enc', 'wb+') as encoded_file:
        encoded_file.write(salt)
        encoded_file.write(nonce)
        encoded_file.write(cipher_message)

def decrypt(encoded_file_path, key_text):

    with open(encoded_file_path, 'rb') as encoded_file:
        salt = encoded_file.read(16)
        nonce = encoded_file.read(16)
        cipher_message = encoded_file.read()
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(key_text.encode())

    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(cipher_message)

    with open(f"{encoded_file_path}.dec", 'wb') as decoded_file:
        decoded_file.write(plaintext)

def main():
    try:
        if sys.argv[1] == 'enc':
            passphrase = input("Enter passphrase: ")
            encrypt(sys.argv[2], passphrase)
        elif sys.argv[1] == 'dec':
            passphrase = input("Enter passphrase: ")
            decrypt(sys.argv[2], passphrase)
        else:
            print("Invalid command. Use 'enc' to encrypt or 'dec' to decrypt.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
