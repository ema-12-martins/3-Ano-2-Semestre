import sys
import vigenere
from itertools import product
from string import ascii_uppercase

probabilidades_letras = {
    'A': 14.63,
    'B': 1.04,
    'C': 3.88,
    'D': 4.99,
    'E': 12.57,
    'F': 1.02,
    'G': 1.30,
    'H': 1.28,
    'I': 6.18,
    'J': 0.40,
    'K': 0.02,
    'L': 2.78,
    'M': 4.74,
    'N': 4.63,
    'O': 9.50,
    'P': 2.52,
    'Q': 1.20,
    'R': 6.53,
    'S': 7.81,
    'T': 4.34,
    'U': 4.63,
    'V': 1.67,
    'W': 0.01,
    'X': 0.21,
    'Y': 0.01,
    'Z': 0.47
}


def main(*args):

    #Verifica se foi passado um numero inteiro
    try:
        tamanho_combinacao = int(args[1])
    except ValueError:
        print("O argumento deve ser um número inteiro")
        sys.exit(1)
    
    #Verifica se o tamanho da chave pode ser o passado como argumento
    if (len(args[2]) < tamanho_combinacao):
        print("A chave nao pode ter esse tamanho")
        sys.exit(1)

    # Gera todas as combinações possíveis de chave para um dado tamanho
    combinações = [''.join(combinação) for combinação in product(ascii_uppercase, repeat=tamanho_combinacao)]
    
    #Ve se a chave da para aquele combinacao
    chaves_possiveis = []
    for chave in combinações:
        resultado = vigenere.main("dec", chave, args[2])
        
        for i in range(3,len(args)):
            if args[i] in resultado:
                chaves_possiveis.append((chave, resultado))
                break

    #Vamos ver qual a mais provavel tendo em consideracao a frequencia em portugues:
    probabilidades_max=1
    chave_resultado=chaves_possiveis[0]
    for (chave,criptograma) in chaves_possiveis:

        probabilidade_atual=1
        for letra in criptograma:
            probabilidade_atual*=probabilidades_letras.get(letra,0)

        if probabilidade_atual>probabilidades_max:
            probabilidades_max=probabilidade_atual
            chave_resultado = (chave,criptograma) 

    print(chave_resultado)

if __name__ == "__main__":
    main(*sys.argv)