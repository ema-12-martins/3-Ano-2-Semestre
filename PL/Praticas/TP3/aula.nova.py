import re
#...........................DADOS.........................
codigos_postais_lista=[
        "4770-000",
        "1234-567",
        "8541-543",
        "9481-025"
    ]

texto = """A 03/01/2022, V foi de férias com a sua família.
Ficaram hospedados num hotel e aproveitaram as férias para passear e descobrir novos locais.
Mais tarde, no dia 12/01/2022, V voltou para casa e começou a trabalhar num novo projeto.
Passou muitas horas no computador, mas finalmente terminou o projeto a 15/01/2022.

Alguns meses depois, a 26/09/2023, V casou-se com Judy e no dia 30/09/2023 partiram na
sua lua-de-mel para o local onde V tinha ido de férias no ano anterior."""

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

mad_libs = """Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA].
Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo.
Talvez os [NOME PLURAL MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""

conversao_nomes = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
do professor Pedro Rangel Henriques e do professor José João Antunes Guimarães
Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""

lista_codigos_postais = [
    "4700-000", # válido
    "9876543", # inválido
    "1234-567", # válido
    "8x41-5a3", # inválido
    "84234-12", # inválido
    "4583--321", # inválido
    "9481-025" # válido
]

abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
}

texto_abreviaturas = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."

#....................................EXERCICIOS..........................................

#Ainda da aula anterior
#EX10
def codigos_postais(lista):
    lista_nova=[]
    for codigo in lista:
        [a,b]=(re.split(r"-",codigo))
        lista_nova.append((a,b))
    return lista_nova

#1-Converte as datas presentes numa string no formato DD/MM/AAAA para o formato ISO 8601 - AAAA-MM-DD
def iso_8601(texto):
    texto_substituido = re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',texto) #O segundo argumento pode ser uma funcao
    return texto_substituido

#2- Escreve um programa que lê uma lista de nomes de ficheiros e determina se cada nome é válido ou não. O nome de um ficheiro deve conter apenas caracteres alfanuméricos, hífens, underscores ou pontos, seguido de uma extensão (e.g., ".txt", ".png", etc.).
def ficheiro_validos(ficheiros):
    lista_resultados=[]
    for ficheiro in ficheiros:
        if re.match(r"[\w|-|\.]+\.\w+",ficheiro):
            lista_resultados.append((ficheiro,"válido"))
        else:
            lista_resultados.append((ficheiro,"inválido"))
    return lista_resultados

#2.1-Modifica o programa anterior para colocar os nomes de ficheiro válidos num dicionário, no qual as chaves deverão ser as extensões dos mesmos.
def ficheiro_validos_dic(ficheiros):
    lista_resultados={}
    for ficheiro in ficheiros:
        if resultado:=re.fullmatch(r"[\w\-\.]+(\.\w+)",ficheiro):
            if resultado.group(1) in lista_resultados:
                lista_resultados[resultado.group(1)].append(ficheiro)
            else:
                lista_resultados[resultado.group(1)]=[ficheiro]
    return lista_resultados

#3- Escreve um filtro de texto que converte cada nome completo de uma pessoa encontrada num texto fonte, no formato PrimeiroNome SegundoNome. Por exemplo, "Rui Vieira de Castro" passa a "Castro, Rui". Atenção aos conectores "de", "dos", etc.
def troca_forma_nome(conversao_nomes):
    novo_texto = re.sub(r"([A-Z]\w+)(?:\s(?:[A-Z]\w+|d[eao]s?))+\s([A-Z]\w+)",r"\2,\1",conversao_nomes)
    #como os nomes podem ter acentos, usamos o \w. o ?: é para nao considerar aquele grupo de captura
    return novo_texto

#4-Define uma função codigos_postais que recebe uma lista de códigos postais e divide-os com base no hífen. Ao contrário do exercício da ficha anterior, esta função pode receber códigos postais inválidos. A função deve devolver uma lista de pares e apenas processar cada linha uma vez.
def valida_cod_postais(lista_codigos_postais):
    expressao_regular=re.compile(r"(\d{4})-(\d{3})")

    lista_codigos_validos=[]
    for elem in lista_codigos_postais:
        if r:=re.match(expressao_regular,elem): #Posso fazer isto com os grupos de captura
            lista_codigos_validos.append((r.group(0),r.group(1)))
    return lista_codigos_validos

#5-Escreve um filtro de texto que expanda as abreviaturas que encontrar no texto fonte no formato "/abrev".
def subs_abreviaturas(texto_abreviaturas):
    return(re.sub("/abrev\{(\w+)\}",lambda m: abreviaturas[m.group(1)] ,texto_abreviaturas)) #m é a correspondencia
    

#7-O jogo Mad Libs, bastante comum em países como os Estados Unidos, consiste em pegar num texto com espaços para algumas palavras e preencher esses espaços de acordo com o tipo de palavra que é pedida.
def prompt(m):
    resposta = input("Introduz um(a)"+ m.group(1)+":")
    return resposta

def mad_libs_func(texto):
    return re.sub(r"\[([^\]]+)\]",prompt,texto) #Qualquer coisa que nao seja os parentices retos de fecho


def main():
    
    #print(codigos_postais(codigos_postais_lista))
    #print(iso_8601(texto))
    #print(ficheiro_validos(file_names))
    #print(ficheiro_validos_dic(file_names))
    #print(mad_libs_func(mad_libs))
    #print(troca_forma_nome(conversao_nomes))
    #print(valida_cod_postais(lista_codigos_postais))
    print(subs_abreviaturas(texto_abreviaturas))

if __name__ == "__main__":
    main()

