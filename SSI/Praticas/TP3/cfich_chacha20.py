import sys
import struct, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def main():
    nonce = os.urandom(8)
    counter = 0
    full_nonce = struct.pack("<Q", counter) + nonce