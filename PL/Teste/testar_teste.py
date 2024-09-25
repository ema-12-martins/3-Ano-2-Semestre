import re 

import re 

def funcao(texto):
    pattern = r'gost[a-z]* (?:de|dos|do|da|das) ([a-z]+)'
    match = re.findall(pattern, texto)
    
    return match

print(funcao('O manel gosta de passear e sempre gostou de praia'))

def funcao2():
    frase = "Ola aaa OLA123ola e tuOla--ola."
    res = re.search( r'[^ ]+?(?i:ola)', frase )
    return len(res)
print(funcao2())
