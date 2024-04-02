# Exemplo
Exemplo

Escrever uma gramática para descrever um dicionário, o qual é formado por uma ou mais entradas.
Cada entrada é um triplo formado pela palavra a ser definida, uma lista de palavras sinónimas e, opcionalmente, um significado que é um texto explicativo dessa palavra.

~~~
GIC = <T,N,S,P>
N:Dicionario, Entradas, Sinonimos, Signif,
S:Dicionario

P:    
Dicionario -> Entradas

Entradas   -> Entrada 
            |  Entrada Entradas

Entrada -> PALAVRA '[' Sinonimos ']' Signif

Sinonimos -> PALAVRA
            |  Sinonimos ',' PALAVRA

Signif -> €
        | TEXTO

tokens = (
    'PALAVRA',
	'TEXTO'
)
~~~

Nao devemos ter recorsividade à direita pois dá conflitos LL(1).

# Exercicio 1
Considere as seguintes frases
    eu= Mara Maria Mendes Almeida.
	Eu =Antonio Cunha Rego.
	ELE =Antonio Silva.

Formalize estas frases escrevendo uma GIC.

~~~
(p1) Entrada -> Pronome'='Nomes'.'

(p2) Pronome -> EU
(p3)          |ELE

(p4) Nomes -> Nome
(p5)        | Nomes Nome

(p6) Nome -> PALAVRA
~~~

Os espacos, o analisador lexico é que tem de tratar de os ignorar ignora.

Para desenhar a arvore de derivação:
~~~
                    Entrada
                       |
        ----------------------------------------
        |              |            |          |
    Pronome          ('=')        Nomes      ('.')
       |                            |
      (EU)                         Nome
                                    |
                                (Palavra)
~~~
Esta arvore resulta, por exemplo: EU = Diogo. ou EU = Ana.
**Os terminais estao representados dentro de parentices.**

Outra arvore possivel:
~~~
                    Entrada
                    |
        ----------------------------------------
        |              |            |          |
    Pronome           ('=')       Nomes       ('.')
       |                            |
      (EU)                         Nome
                                    |
                               ----------------
                               |              |
                             Nomes           Nome
                               |              |
                        -------------       (Palavra)
                        |           |
                       Nomes       Nome
                        |           |
                       Nome       (Palavra)
                        |
                     (Palavra)
~~~
Neste caso, uma frase possivel seria: Eu = Maria Ana Pereira.

A producao desta ultimo exemplo: p2 p6 p4 p6 p4 p5 p6 p4 p5 p1
Vamos fazendo reduções.

# Exercicio 2
Escreva uma GIC para uma biblioteca que tenha pelo menos um livro. Cada livro contem titulo, autor, ano e ISBN.

~~~
(p1) Bibliografia -> Livros

(p2) Livros -> Livro
(p3)         | Livros ';' Livro

(p4) Livro -> Titulo Autor Ano ISBN

(p5) Titulo -> TEXTO

(p6) Autor -> TEXTO

(p7) Ano -> INT
~~~
Os terminais por norma sao escritos com todas as letras maiusculas.

Um exemplo de frase que podemos escrever com esta gramática: 
~~~
"Os Maias" "Eça de Queirós" 1860 1000-312/521;
"Amor de Perdição" "Camilo Castelo Branco" 1862 1000-515/329
~~~

# Exercicio 3

Considere as seguintes frases:
~~~
Joana@4000-987;-12,55;67,98
Rangel.Henriques.Pedro@4715-012;41,55;8,45
Silva.Ana.Maria@4715-012;41,55;-9,00
Araujo.?@4715-767;42,05;-10,35
Mota.Carmo@4780-767;40,05;8,55
~~~
Formalize estas frases escrevendo uma GIC.

# Exercicio 4
Escreva um analisador léxico e um  parser para reconhecer uma linguagem que permita descrever os alunos de uma turma. Por cada aluno deve indicar-se o nome e a lista de notas.

Exemplo:
~~~
Rui : [10,15]
Tiago : [15,12]
~~~


