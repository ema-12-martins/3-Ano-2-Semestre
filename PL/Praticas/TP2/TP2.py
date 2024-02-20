import re

#1.1- Determinar se a palavra 'hello' procura no inicio, dado apenas a primeira ocorrencia
def hello_inicio_frase(line):
    print(re.match(r"hello",line))

#1.2- Determinar se a palavra 'hello' existe na frase, dando apenas a primeira ocorrencia
def hello_no_meio(line):
    print(re.search(r"hello",line))

#1.3- Determinar se a palavra 'hello' existe na frase, retornando todas as ocorrencias
def hello_no_meio_list(line):
    print(re.findall(r"[Hh]ello",line))

#1.4- Susbtituir todas as occorencia da expressao regular por outra espressao
def substitui_hello(line):
    print(re.sub(r"[Hh]ello","*YEP",line,3)) #Ultimo numero so substitui 3x (opcional)

#1.5- Divide a string por uma expressao regual
def split_hello(line):
    print(re.split(r" *, *"),line) #Tambem tem o maximo que queremos dividir

#2- Recebe uma frase e ve se a mesam termina com uma expewssao regular "por favor"
def palavra_magica(frase):
    print(re.search(r"por favor[.!?;]+$",frase,re.I)) #re.I é para aceitar maiusculas e minusculas. O + é por causa de ...

#3- Quantas vezes a palavra "eu" aparece na frase
def narcissismo(linha):
    print(len(re.findall(r"[Ee][Uu]",linha)))

#4- Troca o curso LEI quando aparece por outro curso
def troca_de_curso(linha, novo_curso):
    print(re.sub(r"LEI",novo_curso,linha))

#5- Recebe uma string com varios numeros separados por virgula de numeros e devolve a soma
def soma_string(linha):
    print(sum(map(int,re.split(r" *, *",linha))))
    
#6- Encontra e devolve todos os pronomes pessoais presentes numa frase, i.e., "eu", "tu", "ele", "ela", etc., com atenção para letras maiúsculas ou minúsculas
def pronomes(linha):
    print(re.findall(r"\b(el[ae]s?|vós|nós|eu|tu)\b", linha, flags=re.IGNORECASE)) #/b que aquilo tem de ser uma palavra

#7- Recebe uma string e determina se a mesma é um nome válido para uma variável, ou seja, se começa por uma letra e apenas contém letras, números ou underscores.
def valida_variavel(variavel):
    print(re.search(r"^[a-z][a-z_0-9]*$",variavel,flags=re.IGNORECASE))


def main():
    line1 = "hello world"
    line2 = "goodbye world"
    line3 = "hi, hello there"

    palavra_magica1 = "Posso ir à casa de banho, por favor?"
    palavra_magica2="Preciso de um favor."
    palavra_magica3= "Sim, por favor, obrigado."

    frase_narcissismo="Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."
    frase_troca_curso="LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei."
    string_numeros="4,-6,2,3,8,-3,0,2,-5,1"
    string_pronomes="Ola a ela, a ele e a eles. Somos nós os melhores. Eu tambem"
    string_variavel="A_sd"

    palavra_magica(palavra_magica1)
    narcissismo(frase_narcissismo)
    troca_de_curso(frase_troca_curso,"LEBIOM")
    soma_string(string_numeros)
    pronomes(string_pronomes)
    valida_variavel(string_variavel)
    
if __name__ == "__main__":
    main()