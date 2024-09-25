import sys
import random

def bad_prng(n, seed):
    random.seed(seed)
    return random.randbytes(n)

def main():
    arquivo_criptografado = sys.argv[1]
    palavras = set(sys.argv[2:])

    # Abre o arquivo com o criptograma
    with open(arquivo_criptografado, "rb") as f:
        criptograma = f.read()

    # Percorre todas as sementes do gerador aleatório
    for seed in range(2**16):
        chave = bad_prng(len(criptograma), seed)

        texto_decifrado = bytes(a ^ b for a, b in zip(criptograma, chave)).decode(errors='ignore')

        if any(palavra in texto_decifrado for palavra in palavras):
            print(f"Chave encontrada: {seed}")
            return

    print("Chave não encontrada.")

if __name__ == "__main__":
    main()
