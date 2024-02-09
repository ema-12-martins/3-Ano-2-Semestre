#...................REVISOES DE PYTHON..............

#1
d={
    "bananas":4,
    "melancias":5
}
print(d["bananas"]) # Imprime 4
print(d.get("peras")) # Como peras nao existe imprime None
print(d.get("melancias")*3) #Imprime 15
print(d.get("peras","nao existe")) # Como peras nao existe imprime nao existe

#Listas VERRRRRRRRRRRR LISTASSSSSSSSSSss
l1=[5:12]
l2=[-3:]
l3=[::3]
l4=[3::-1]
l5=[x*2 for x in range(1,10) if x%2==0]

#Quase estamso em programacao funcional
match lista:
    case [1,2,3]: print("A lista é [1,2,3]")
    case [1,*t] | [_,_]: print("Lista comeca com 1 ou tem 2 elmentos") #*t revolver a cauda
    case _: print("Nao conheco esta lista")

Nota: em pyton nao existe ++ nem --.
Nota: lista.clean() Elimina tudo da lista
    l2=l1.copy() Copia

for i, cor in enumerate(cores2): #Associa (num,elemento)

#VER A CENA DE JUNTAR TUDO NUM TUPLO
    
dobros=map(lambda x: x*2,range(1,6)) # obetemos [2,4,6,8,10]
evens = filter(l,isEven)
reduce(lambda acc,x) # ver isto

# Ficheiros
content= open("input.txt","rt") #t para etxto e b para binario
linhas = f.readlines

linah1=f.readline()
linah2 = f.readline

f.write()

# Classes
As classes tem de ter __init__(self,..), __str__(self)
Os atributos das classes tem de ser publicos, nao ha opcao

#VER ENUMS

#Exercicios 1
Defina a funcao drequencia que dada uma frase, calcula a frequencia de todas as palavras.
def freqencia(frase):
    palavras=map(lambda palavra: ''.join(filter(x.isalpha(),frase.split()))) #isalpha #split sem algumentos divide por espacoes e \n Podemos por .lower para meter minusculas
    freq=dict()
    for palavra in palavra:
        if palavra in freq:
            freq[palavra]+=1
        else:
            freq[palavra]=1
    return freq

#Para ser se codigos postais sao validos
def processa(codigos_postais):
    validos=[]
    for codigo in codigos_postais:
        match codigo.split("-")
            case [p1,p2]:
                if p1.isdigit() and p2.isdigit() and len(p1)==4 and len(p2)==3:
                    validos.append((p1,p2))
            case _ : continue 
    

lista=[] #copiar lista
