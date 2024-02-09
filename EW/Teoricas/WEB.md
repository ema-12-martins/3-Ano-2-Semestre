# Encoding
Tabela de correspondência que assoica um código a um símbolo.
1. ASCII - Usa 1 byte. 7 bites representam informação e outro a paridade. (1 byte)
2. Unicode - Usado para generalizar para todos os alfabeto, mais caracteres. Como exemplo, temos o utf-8 e o uft-16.

Nota: No mongobd só funciona com datasets em json.

# Formatos de texto
CSV - Primeira linha é um cabeçalho que descreve as colunas. As linhas acabam com \n e os elementos estao separados com o ;. Tem apenas duas dimenssões e é estruturado.

JSON - É uma lista com dicionários. Ex: [{"Estado": "","Codigo":"900"...}]. Pode ter N dimenssões e é estruturado.

XML - Pode ter n dimenssões e é semi-estruturado.

# Exemplo de funcionamento do json
Temos uma turma que tem alunos. Cada aluno tem associado um nome, um id e um conjunto de notas. Como podemos formatar esta informação em json?
Maria;A22327;15;13;14
Zé;A99133;12;17;18

Esta é uma possível solução com 3 dimensões:
~~~
[{"Nome":"Maria","id":"A22327","notes":[15,13,14]},{"Nome":"Zé","id":"A99133","notes":[12,17,18]}]
~~~

Assumindo que o ficheiro turma.json contém a turma, como podemos, em python, dizer todos os nomes dos alunos da turma, ordenados alfabeticamente?
~~~
import json

f=open("turma.json")
turma = json.load(f)

nomes = []
for aluno in turma:
    nomes.append(aluno['nome'])

nomes.sort
print(nomes)
~~~

# Revisões de Python
Se quisermos fazer um dicionario em que a chave seja o numero de um elemento numa lista, como o poderiamos fazer?
~~~
lista = ["ola","ola"] #Poderia ter mais elementos
dic1 = dict(enumerate(lista)) #O enumerate cria uma lista de tuplos em que o primeiro número é a posição do elemento.
~~~

Teriamos então como resultado: {1:"ola",2:"ola"}

# HTML
~~~
<html>
    <head>
        <title> A minha primeira pagina </title>
        <link rev="made"
            href="mailto:jrc@di.uminho.pt"/>
    </head>
    <body>
        <!--Para fazer comentarios-->
        ...Aqui aparece o conteudo...
    </body>
</html>

~~~
Temos tags de abertura e fecho. As self-tags não tem conteudo textual pelo que não terminam e com />. Na tag de abertura podemos ter atributos.

Paragrafos faz-se com a tag <p>. Os cabeçalhos com a tag <hx> em que x pode ir de 1 a 6. O número escolhido muda o tamanho da letra do título. <i> para itálico e <b> bolt. <code> para meter codigo. Podemos colocar ainda links nas tags com o atributo <a ...>.

Temos ainda listas em html.
~~~
<ol> <!--Lista ordenada-->
    <li> primeiro elemento </li>
    <li>segubdo elemento </li>
<ol>

<dl> <!--Lista dicionario-->
    <dt>descricao </dt>
    <dd>valor </dd>
<dl>

<ul> <!--Lista sem ordem --> 
    <li> primeiro elemento </li> 
    <li>segubdo elemento </li>
<ul>
~~~

# URL 
Localizador de uma página web. Este segue o seguinte protcolo/formato: //host/dir/subdir/.../filename. **Exemplo**: http://www.di.uminho.pt/~jcr/engweb.html#aval

O # leva permite-nos navegar para uma parte da página.

Tipos dos elementos:
Os **inline** são difernetes dos **block** porque levam uma quebra de linha depois e antes.

Inline: span,b,i...
Block: div,p

Nota: A div só tem valor se tiver associado ao style. O span é semelhante.
