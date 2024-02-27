import sys
import random

def bad_prng(n):
    random.seed(random.randbytes(2))
    return random.randbytes(n)

def main(*args):
    if args[1] == "setup":
        num_bytes_a_gerar = int(args[2])
        nome_ficheiro_guarda_chave = args[3]

        with open(nome_ficheiro_guarda_chave, "wb") as ficheiro:
            chave=bad_prng(num_bytes_a_gerar)
            print(chave)
            ficheiro.write(chave)
    
    elif args[1] == "enc" or args[1] == "dec":
        ficheiro_com_criptograma = args[2]
        ficheiro_com_chave = args[3]

        with open(ficheiro_com_chave, "rb") as ficheiro_chave:
            chave = ficheiro_chave.read()

        with open(ficheiro_com_criptograma, "rb") as ficheiro_criptograma:
            criptograma = ficheiro_criptograma.read()

        # Se o criptograma estiver em texto, converta para bytes
        if isinstance(criptograma, str):
            criptograma = criptograma.encode()

        # Fazer o XOR bit a bit entre o criptograma e a chave
        texto = bytes(a ^ b for a, b in zip(criptograma, chave))

        # Se o resultado for texto, decode para string
        if args[1] == "dec":
            texto = texto.decode()

        # Guardar o resultado em um novo arquivo
        if args[1] == "enc":
            with open(f"{ficheiro_com_criptograma}.enc", "wb") as ficheiro_cifrado:
                ficheiro_cifrado.write(texto)
        else:
            with open(f"{ficheiro_com_criptograma}.dec", "w") as ficheiro_cifrado:
                ficheiro_cifrado.write(texto)

if __name__ == "__main__":
    main(*sys.argv)