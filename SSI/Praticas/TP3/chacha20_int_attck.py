import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# This attack is supposed to change some letters in the cipher_text
def attack(cipher_text_file_path, position, text_in_the_position, new_text):
    with open(cipher_text_file_path, 'rb') as cipher_text_file:
        nonce=cipher_text_file.read(16)
        cipher_text = bytearray(cipher_text_file.read()) #Because it's an array of bytes, it is immutable

    position=int(position)
    new_text=new_text.encode()
    text_in_the_position=text_in_the_position.encode()
    for i in range(len(text_in_the_position)):
        cipher_text[position + i] ^= text_in_the_position[i]
        cipher_text[position + i] ^= new_text[i]
        
    with open(f"{cipher_text_file_path}.attck", 'wb') as plaintext_file:
        plaintext_file.write(nonce)
        plaintext_file.write(cipher_text)


def main():
        attack(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()
