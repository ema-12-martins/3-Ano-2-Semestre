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

def ex15(texto):
    pattern=r'(\d{2})/(\d{2})/(\d{4})'
    return re.sub(pattern,r'\3-\2-\1',texto)

def ex16(lista):
    pattern=r'[\w\-\.]+\.(txt|png|docx|jpg)'
    lista_corretos=[]

    for elem in lista:
        match = re.match(pattern,elem)
        if(match!=None):
            lista_corretos.append(elem)

    return lista_corretos

def ex17(lista):
    pattern=r'[\w\-\.]+\.(txt|png|docx|jpg)'
    dic_corretos={}

    for elem in lista:
        match = re.match(pattern,elem)
        if(match!=None):
            if match.group(1) in dic_corretos.keys():
                dic_corretos[match.group(1)].append(elem)
            else:
                dic_corretos[match.group(1)]=[elem]

    return dic_corretos

def ex18(texto):
    pattern = r'([A-Z][a-z]+(?: (?:de|dos)? [A-Z][a-z]+)*) ([A-Z][a-z]+)'
    return re.sub(pattern, r'\2, \1', texto)

def ex19(lista):
    pattern=r'([0-9]{4})-([0-9]{3})'
    list_result = []

    for i in range(len(lista)):
        result= re.search(pattern,lista[i])
        if(result!=None):
            list_result.append((result.group(1),result.group(2)))
    return list_result

def auxEx20(match, dic):
    campo = match.group(1)
    if campo in dic:
        return dic[campo]
    else:
        return 'NONE'

def ex20(texto, dic):
    pattern = r'/abrev\{([a-zA-z]+)\}'
    return re.sub(pattern, lambda match: auxEx20(match, dic), texto)

def ex21(lista):
    lista_matriculas_validas=[]
    pattern=r'\d{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-\d{2}|[A-Z]{2}-\d{2}-\d{2}|[A-Z]{2}-[A-Z]{2}-\d{2}|[A-Z]{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-[A-Z]{2}'

    for elem in lista:
        if re.match(pattern,elem)!=None:
            lista_matriculas_validas.append(elem)
    
    return lista_matriculas_validas

def auxEx22(match):
    variavel = input('Escreva '+match.group(1)+': ')
    return variavel
    
def ex22(texto):
    pattern=r'\[(.*?)\]'
    return re.sub(pattern,auxEx22,texto)

import re

lista_palavras = []

def auxEx23(match):
    global lista_palavras

    if match.group(0) not in lista_palavras:
        lista_palavras.append(match.group(0))
        return match.group(0)
    else:
        return ''

def ex23(texto):
    pattern = r'[a-zA-Z]+'
    return re.sub(pattern, auxEx23, texto)

# Exemplo de uso:
texto = "Isso é um teste teste para verificar repetições repetições."
print(ex23(texto))  # Saída esperada: "Isso é um teste para verificar repetições."

        
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

print('...............EX15.............')
print(ex15('Hoje, dia 23/05/1987 está calor como em 04/12/1776'))

print('...............EX16.............')
file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg" # inválido
]
print(ex16(file_names))

print('...............EX17.............')
print(ex17(file_names))

#Alguma coisa esta errada

print('...............EX18.............')
texto = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
do professor Pedro Rangel Henriques e do professor José João Antunes Guimarães
Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""
print(ex18(texto))

print('...............EX19.............')
lista_codigos_postais = [
    "4700-000", # válido
    "9876543", # inválido
    "1234-567", # válido
    "8x41-5a3", # inválido
    "84234-12", # inválido
    "4583--321", # inválido
    "9481-025" # válido
]
print(ex19(lista_codigos_postais))

print('...............EX20.............')
abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
}

print(ex20("A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito.",abreviaturas))

print('...............EX21.............')
matriculas = [
    "AA-AA-AA", # inválida
    "LR-RB-32", # válida
    "1234LX", # inválida
    "PL 22 23", # válida
    "ZZ-99-ZZ", # inválida
    "54-tb-34", # inválida
    "12 34 56", # inválida
    "42-HA BQ" # válida, mas inválida com o requisito extra
]
print(ex21(matriculas))

print('...............EX22.............')
#print(ex22('Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA].Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].Ficaram muito confusos, pois não conseguiam identificar a função daquilo.'))

print('...............EX23.............')
print(ex23('será será repetida muitas muitas vezes. Gosto muito muito.'))