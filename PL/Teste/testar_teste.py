import re 

import re 

def funcao(texto):
    pattern = r'gost[a-z]* (?:de|dos|do|da|das) ([a-z]+)'
    match = re.findall(pattern, texto)
    
    return match

print(funcao('O manel gosta de passear e sempre gostou de praia'))
