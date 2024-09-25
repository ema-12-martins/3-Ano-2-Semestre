import sys
import os
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

def encrypt(plaintext_file_path, key_text):
    # Open the plaintext file in binary mode and read its contents
    with open(plaintext_file_path, 'rb') as plaintext_file:
        plaintext = plaintext_file.read()

    # Generate a random salt
    salt = os.urandom(16)
    # Derive a key using PBKDF2 with SHA256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(key_text.encode())
    #key = ChaCha20Poly1305.generate_key()
    chacha = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    cipher_message = chacha.encrypt(nonce, plaintext, None)

    # Write salt, IV, and signature to the encrypted file
    with open(f'{plaintext_file_path}.enc', 'wb+') as encoded_file:
        encoded_file.write(salt)
        encoded_file.write(nonce)
        encoded_file.write(cipher_message)

def decrypt(encoded_file_path, key_text):
    # Read salt, IV, and ciphertext from the encrypted file
    with open(encoded_file_path, 'rb') as encoded_file:
        salt = encoded_file.read(16)
        nonce=encoded_file.read(12)
        cipher_message = encoded_file.read()

    # Derive the key using the same salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(key_text.encode())
    chacha = ChaCha20Poly1305(key)

    decrypted_data = chacha.decrypt(nonce, cipher_message, None)


    # Write decrypted data to the output file
    with open(f"{encoded_file_path}.dec", 'wb') as decoded_file:
        decoded_file.write(decrypted_data)

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
