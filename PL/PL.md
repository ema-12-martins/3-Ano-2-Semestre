# Exercicio Inicial
O que é que o seguinte código imprime?
~~~
d={
    "bananas":4,
    "melancias":5
}
print(d["bananas"]) 
print(d.get("peras")) #Peras nao existe
print(d.get("melancias")*3) 
print(d.get("peras","nao existe")) #Peras nao existe 
~~~
Irá imprimir na consola:
~~~
4
None
15
nao existe
~~~

#Listas (FALTAM COISAS)
~~~
l1=l[5:12] #Lista do 5 ao 11 elemento
l2=l[-3:] #Lista com os ultimos 3 elementos
l3=l[::3] #lista com os elementos da lista principal espacados de 3 em 3
l4=l[3::-1] #Cria uma lista invertida da l nas posicoes fornecidas
l5=[x*2 for x in range(1,10) if x%2==0] #Lista em compreenssao que da os elementos pares entre 1 e 9
~~~

# Quase que estamos em programacao funcional...
As versões mais atuais do Python permitem fazer o seguinte comando:
~~~
match lista:
    case [1,2,3]: print("A lista é [1,2,3]")
    case [1,*t] | [_,_]: print("Lista comeca com 1 ou tem 2 elmentos") #*t revolver a cauda
    case _: print("Nao conheco esta lista")
~~~

Nota: Em Pyton nao existe ++ nem --. Quando queremos incrementar ou decrementar uma unidade temos de fazer i+=1 ou i-=1.

# Coisas que dao jeito saber em Python
- O método **l.clean()** elimina tudo o conteudo de uma lista.
- O método **l.copy()** copia toda a lista l.
- A função **enumerate(l)** cria um tuplo com o indice do elemento e o valor dele na lista ((num,elemento)). Isto permite fazer:
~~~
for i, cor in enumerate(cores2): 
~~~

#VER A CENA DE JUNTAR TUDO NUM TUPLO
    
#Funcoes de ordem superior em Python
~~~
dobros=map(lambda x: x*2,range(1,6)) 
~~~
Este codigo dará a lista [2,4,6,8,10].

~~~
lista = [1, 2, 3, 4, 5]
evens = filter(l,isEven)
~~~
Este código dará a lista [2,4].

~~~
lista = [1, 2, 3, 4, 5]
soma = reduce(lambda acc, x: acc + x, lista)
~~~
Este código dará 15.

# Ficheiros
~~~
content= open("input.txt","rt") #t para ficheiros de texto e b para binarios
linhas = f.readlines #Faz uma lista de listas em que cada elemento é uma linha.
~~~
Ao invés de lermos todas as frases do ficheiro, podemos querer ler linha a linha. Isso faz-ze com o seguinte código:
~~~
linah1=f.readline() #Lê apenas uma linha
linah2 = f.readline() #Lê a linha seguinte
~~~

Podemos ainda querer escrever para o ficheiro. Para isso:
~~~
f= open("output.txt","wt")
f.write()
f.close()
~~~
Devemos sempre fechar os ficheiros quando já não os estivemos a usar.

# Classes
As classes tem de ter \_\_init\_\_(self,..), _\_\str_\_\(self)
Os atributos das classes tem de ser publicos, nao ha opcao.

# VER ENUMS

## Exercicios 1
Defina a funcao **frequencia** que dada uma frase, calcula a frequencia de todas as palavras.
~~~
def freqencia(frase):
    palavras=map(lambda palavra: ''.join(filter(x.isalpha(),frase.split()))) #isalpha #split sem algumentos divide por espacoes e \n Podemos por .lower para meter minusculas
    freq=dict()
    for palavra in palavra:
        if palavra in freq:
            freq[palavra]+=1
        else:
            freq[palavra]=1
    return freq
~~~

## Exercicio 2
Defina a funcao **processa** que valida codigos postais.
~~~
def processa(codigos_postais):
    validos=[]
    for codigo in codigos_postais:
        match codigo.split("-")
            case [p1,p2]:
                if p1.isdigit() and p2.isdigit() and len(p1)==4 and len(p2)==3:
                    validos.append((p1,p2))
            case _ : continue 
~~~
