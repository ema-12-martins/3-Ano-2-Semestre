import sys
import os
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

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

    # Generate a random IV
    iv = os.urandom(16)

    # Encrypt the plaintext using AES in CTR mode
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    cipher_message = encryptor.update(plaintext) + encryptor.finalize()
    

    # Calculate HMAC signature for integrity verification
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(cipher_message)
    signature = h.finalize()

    # Write salt, IV, and signature to the encrypted file
    with open(f'{plaintext_file_path}.enc', 'wb+') as encoded_file:
        encoded_file.write(salt)
        encoded_file.write(iv)
        encoded_file.write(signature)
        encoded_file.write(cipher_message)

def decrypt(encoded_file_path, key_text):
    # Read salt, IV, and ciphertext from the encrypted file
    with open(encoded_file_path, 'rb') as encoded_file:
        salt = encoded_file.read(16)
        iv = encoded_file.read(16)
        signature = encoded_file.read(32)  # HMAC signature length is 32 bytes
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

    # Verify HMAC signature for integrity verification
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(cipher_message)
    h.verify(signature)

    # Decrypt the ciphertext using AES in CTR mode
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(cipher_message) + decryptor.finalize()

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
