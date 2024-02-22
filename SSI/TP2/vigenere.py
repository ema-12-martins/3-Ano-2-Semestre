import sys

def preproc(str):
    l = []
    for c in str:
        if c.isalpha():
            l.append(c.upper())
    return "".join(l)  

def main(tipo_operacao, cifra, frase):
    frase = preproc(frase)
    cifra = preproc(cifra)

    resultado = ""
    if tipo_operacao == "enc":
        posicao_cifra = 0
        for i in range(len(frase)):
            novo_char = chr(((ord(frase[i]) - 65) + (ord(cifra[posicao_cifra]) - 65)) % 26 + 65)
            resultado += novo_char
            posicao_cifra = (posicao_cifra + 1) % len(cifra)
        
    elif tipo_operacao == "dec":
        posicao_cifra = 0
        for i in range(len(frase)):
            novo_char = chr(((ord(frase[i]) - 65) - (ord(cifra[posicao_cifra]) - 65)) % 26 + 65)
            resultado += novo_char
            posicao_cifra = (posicao_cifra + 1) % len(cifra)
        
    return resultado

if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2], sys.argv[3]))
