# Expressões Regulares
Alguns conceitos de expressões regulares:
- **a** corresponde ao caracter a
- **a*** corresponde a 0 ou mais ocorrencias do caracter a
- **a+** corresponde a 1 ou mais ocorrencias do caracter a
- **[abc]** corresponde a uma ocorrencia dos caracteres a b ou c
- **[a-z]** corresponde aos caracteres de a a z
- **^** corresponde ao inicio de uma string
- **$** corresponde ao fim de uma string
- **[^abc]** corresponde a qualquer ocorrencia desde que não seja a, b ou c
- **b{3}** temos 3 ocorrenacias de b
- **(a)** para formar grupos de captura
- **(?i:teste)** para apanhar casos sem ter em conta de é maiuscula ou minuscula
- **a?** torna a opcional
- **w** alfanumericos (a-z,A-z,0-9,_)
- **\W** nao alfanumerico 
- **\s** whitespace (' ', '\t', ou '\n', por exemplo).
- **\S** caracter que não seja whitespace.
- **\d** dígito.
- **\D** não dígito.

Podemos usar grupos de captura em expressões regulares para isolar segmentos da string capturada. Usamos parênteses para definir grupos de captura. Se colocarmos **?:** num grupo, este deixa de ser um grupo de captura.

~~~ python
import re

m = re.search(r'(2[0-3]|[0-1][0-9]):([0-5][0-9])', "a hora é 13:49")

print(m.groups()) # conjunto dos grupos de captura
print(m.group(0)) # toda a string capturada
print(m.group(1)) # o primeiro grupo de captura
~~~

Podemos, através do operador **?**, torná-los preguiçosos (lazy).

# Modulo RE
O método **match** procura um padrão no início de uma string.
~~~ python
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "123abc456"
match = re.match(pattern, text)

if match:
    print("Match encontrado:", match.group())  # Saída: 123
else:
    print("Nenhum match encontrado.")
~~~

O método **search** procura pelo padrão em qualquer posição da string.
~~~ python
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456"
search = re.search(pattern, text)

if search:
    print("Search encontrado:", search.group())  # Saída: 123
else:
    print("Nenhum search encontrado.")
~~~

O método **compile** compila um padrão regex em um objeto regex, que pode ser reutilizado.
~~~ python
import re

pattern = re.compile(r"\d+")  # Compila o padrão para encontrar um ou mais dígitos
text = "abc123def456"
search = pattern.search(text)

if search:
    print("Search encontrado:", search.group())  # Saída: 123
else:
    print("Nenhum search encontrado.")
~~~

O método **findall** retorna todas as ocorrências não sobrepostas do padrão em uma string.
~~~ python 
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456ghi789"
all_matches = re.findall(pattern, text)
print("Findall encontrado:", all_matches)  # Saída: ['123', '456', '789']
~~~

O método split divide uma string pelo padrão especificado.
~~~python 
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456ghi789"
split_text = re.split(pattern, text)
print("Split resultado:", split_text)  # Saída: ['abc', 'def', 'ghi', '']
~~~

O método **sub** substitui todas as ocorrências do padrão por uma string de substituição.
~~~ python
import re

pattern = r"\d+"  # Padrão para encontrar um ou mais dígitos
text = "abc123def456ghi789"
replaced_text = re.sub(pattern, "#", text)
print("Sub resultado:", replaced_text)  # Saída: abc#def#ghi#
~~~

# Exercicos

1. Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece no início da linha.

2. Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece em qualquer posição da linha.

3. Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, admitindo que a palavra seja escrita com maiúsculas ou minúsculas.

4. Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, substituindo cada uma por "*YEP*".

5. Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências do caracter vírgula, separando cada parte da linha por esse caracter.

6. Define a função palavra_magica que recebe uma frase e determina se a mesma termina com a expressão "por favor", seguida de um sinal válido de pontuação.

7. Define a função narcissismo que calcula quantas vezes a palavra "eu" aparece numa string.

8. Define a função troca_de_curso que substitui todas as ocorrências de "LEI" numa linha pelo nome do curso dado à função.

9. Define a função soma_string que recebe uma string com vários números separados por uma vírgula (e.g., "1,2,3,4,5") e devolve a soma destes números.

10. Define a função pronomes que encontra e devolve todos os pronomes pessoais presentes numa frase, i.e., "eu", "tu", "ele", "ela", etc., com atenção para letras maiúsculas ou minúsculas.

11. Define a função variavel_valida que recebe uma string e determina se a mesma é um nome válido para uma variável, ou seja, se começa por uma letra e apenas contém letras, números ou underscores.

12. Define a função inteiros que devolve todos os números inteiros presentes numa string. Um número inteiro pode conter um ou mais dígitos e pode ser positivo ou negativo.

13. Define a função underscores que substitui todos os espaços numa string por underscores. Se aparecerem vários espaços seguidos, devem ser substituídos por apenas um underscore.

14. Define a função codigos_postais que recebe uma lista de códigos postais válidos e divide-os com base no hífen. A função deve devolver uma lista de pares.

15. Define a função iso_8601 que converte as datas presentes numa string no formato DD/MM/AAAA para o formato ISO 8601 - AAAA-MM-DD, usando expressões regulares e grupos de captura.

16. Escreve um programa que lê uma lista de nomes de ficheiros e determina se cada nome é válido ou não. O nome de um ficheiro deve conter apenas caracteres alfanuméricos, hífens, underscores ou pontos, seguido de uma extensão (e.g., ".txt", ".png", etc.).

17. Modifica o programa anterior para colocar os nomes de ficheiro válidos num dicionário, no qual as chaves deverão ser as extensões dos mesmos. Por outras palavras, agrupa os ficheiros por extensão.

18. Escreve um filtro de texto que converte cada nome completo de uma pessoa encontrada num texto fonte, no formato PrimeiroNome SegundoNome [...] UltimoNome para o formato UltimoNome, PrimeiroNome. Por exemplo, "Rui Vieira de Castro" passa a "Castro, Rui". Atenção aos conectores "de", "dos", etc.

19. Define uma função codigos_postais que recebe uma lista de códigos postais e divide-os com base no hífen. Ao contrário do exercício da ficha anterior, esta função pode receber códigos postais inválidos. A função deve devolver uma lista de pares e apenas processar cada linha uma vez.

20. Escreve um filtro de texto que expanda as abreviaturas que encontrar no texto fonte no formato "/abrev".

21. Define uma função matricula_valida que recebe uma string de texto e determina se esta contém uma matrícula válida. Uma matrícula segue o formato AA-BB-CC, no qual dois dos três conjuntos devem ser compostos por números e o terceiro por letras maiúsculas (por exemplo, 01-AB-23), ou o novo formato no qual dois dos conjuntos são compostos por letras maiúsculas e o terceiro por números (por exemplo, 89-WX-YZ). Os conjuntos podem ser separados por um hífen ou um espaço.

22. O jogo Mad Libs, bastante comum em países como os Estados Unidos, consiste em pegar num texto com espaços para algumas palavras e preencher esses espaços de acordo com o tipo de palavra que é pedida. Escreve um programa que lê um texto no formato Mad Libs e pede ao utilizador para fornecer palavras que completem corretamente o texto.

23. Escreve um filtro de texto que sempre que encontrar no texto fonte uma palavra repetida elimina as repetições, ou seja, substitui a lista de palavras por 1 só palavra.