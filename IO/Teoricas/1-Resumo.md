# Método Simplex
Metodo iterativo que gera uma sequencia de solucoes admissiveis até atingir a solucao otima. Este método, ao invez de usar inequacoes, usa equacoes.

## Transformacao na forma standard
Qualquer inequacao pode ser transformada numa equacao quivalente, introduzindo uma variavel adicional, designada por **variavel de folga**, com valor nao negativo.

~~~
3(x1) + 2(x2) <= 120
(x1),(x2) >= 0
~~~
~~~
3(x1) + 2(x2) + 1(s1) = 120
(x1),(x2),(x3) >= 0
~~~
Temos entao que o recurso disponivel é 120, que 3(x1) + 2(x2) é a quantidade de cada recurso usado e que (s1) e quantidade nao usada do recurso.

Agora imaginemos um sistema de equaçoes
~~~
3(x1) + 2(x2) + 1(s1) + 0 + 0 = 120
1(x1) + 2(x2) + 0 + 1(s2) + 0 = 80
1(x1) + 0 + 0 + 0 + 1(s3) = 30
~~~
Substituindo x1 nas duas euqcoes anteriores, e tendo em consideracao que 1(x1) + 1(s3) = 30 <=> 1(x1)=30-1(s1)
~~~
0 + 2(x2) + 1(s1) + 0 + -3(s3) = 30
0 + 2(x2) + 0 + 1(s2) -1(s3) = 50
1(x1) + 0 + 0 + 0 + 1(s3) = 30
~~~
Podemos observar que obdecem a sistemas equivalentes de equacoes.
Os sistemas poderiam ser escritos como:
~~~
(s1) = 120 -3(x1) -2(x2)
(s2) = 80 -1(x1) -2(x2)
(s3) = 30 -1(x1)
~~~
~~~
(s1) = 30 -2(x2) + 3(s3)
(s2) = 50 -2(x2) + 1(s3)
(x1) = 30 -1(s3)
~~~

A solucao  basica de um sistema de equancoes tem as variaveis independentes a 0 e as dependentes determinados pela resolucao do sistema de equacoes.
~~~
xa=(x1,x2,s1,s2,s3)=(0,0,120,80,30)
xb=(x1,x2,s1,s2,s3)=(30,0,30,50,0)
~~~
Note-se que vamos chamar **variavies basicas** as variavies dependentes e **variavies nao basicas** as variavies independentes. 

---

Fazendo isto para as outras variavies obtemos:
~~~
(s1) = 180 -3(x1) -2(x2)
s2 = 80 -1(x1) -2(x2)
s3 = 30 -1(x1)
z = 0 + 12(x1) + 10(x2)
~~~

A solucao basica é (0,0,120,80,30) e z=0. Conseguimos ter uma melhor solucao se aumentarmos x1. Vamos aumentar o maximo possivel e depois vamos usar o metodo de eliminacao de gauss para reescrever.

Fazemos este processo com outra variavel...