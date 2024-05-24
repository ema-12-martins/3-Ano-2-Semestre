import re

def ex1(texto):
    pattern = r'(?i)hello'
    return re.match(pattern,texto)

def ex2(texto):
    pattern=r'(?i)hello'
    return re.search(pattern,texto)

def ex3(texto):
    pattern=r'(?i)hello'
    return re.findall(pattern,texto)

def ex4(texto):
    pattern=r'(?i)hello'
    return re.sub(pattern,'*YEP*',texto)

def ex5(texto):
    pattern=r','
    return re.split(pattern,texto,maxsplit = 0)

def ex6(texto):
    pattern = r'(?i)por favor(\.{3}|[\.!?])$'
    return re.search(pattern,texto)

def ex7(texto):
    pattern= r'(?i)eu'
    lista = re.findall(pattern,texto)
    return len(lista)

def ex8(texto,curso):
    pattern=r'(?i)LEI'
    return re.sub(pattern,curso,texto)

def ex9(texto):
    pattern=r','
    lista = re.split(pattern,texto)

    contador=0
    for elem in lista:
        contador+=int(elem)

    return contador
    
def ex10(texto):
    pattern=r'(?i)eu|tu|ele|nos|vos|eles'
    return re.findall(pattern,texto)

def ex11(texto):
    pattern=r'(?i)^[a-z][a-z0-9_]*$'
    return re.search(pattern,texto)

def ex12(texto):
    pattern=r'[\+-]?[0-9]+'
    return re.findall(pattern,texto)

def ex13(texto):
    pattern=r'\s+'
    return re.sub(pattern,'_',texto)

def ex14(lista):
    pattern=r'([0-9]{4})-([0-9]{3})'
    list_result = []

    for i in range(len(lista)):
        result= re.search(pattern,lista[i])
        list_result.append((result.group(1),result.group(2)))
    return list_result
        
print('...............EX1.............')
print(ex1('Hello coisas lindas'))
print(ex1('meu deus, ao tempo, hello'))

print('...............EX2.............')
print(ex2('meu deus, ao tempo, hello'))
print(ex2('meu deus, ao tempo'))

print('...............EX3.............')
print(ex3('meu deus, ao tempo, hello'))
print(ex3('hello outra vez, meu deus, ao tempo, hello'))

print('...............EX4.............')
print(ex4('Hello outra vez, meu deus, ao tempo, hello'))

print('...............EX5.............')
print(ex5('Hello outra vez, meu deus, ao tempo, hello'))

print('...............EX6.............')
print(ex6('Coisas preciso de facas, por favor.'))
print(ex6('Nao digas coisas dessas, favor.'))
print(ex6('Nao por favor. Coisas dessas por favor...'))

print('...............EX7.............')
print(ex7('Eu gosto muito de eu propria coisa que eu adoro'))

print('...............EX8.............')
print(ex8('Eu gosto muito de LEi lei LEIIIIIII','BIOMEDICA'))

print('...............EX9.............')
print(ex9('1,2,3'))

print('...............EX10.............')
print(ex10('eu e tu somos nos'))

print('...............EX11.............')
print(ex11('AnaMaskcksdnc_'))
print(ex11('234naMaskcksdnc'))

print('...............EX12.............')
print(ex12('-23 sdkcks csd34dvd +2dfdc'))

print('...............EX13.............')
print(ex13('asdfkd ksdck   skd skdc '))

print('...............EX14.............')
print(ex14(['3456-234','3454-456','2345-456']))
