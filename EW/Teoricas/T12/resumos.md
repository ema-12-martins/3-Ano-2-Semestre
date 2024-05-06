# Comandos
~~~
sudo npx express generator --view=pug autenticacao
npm i
~~~

# Cokkies
Ficheiro que é armazenado no nosso pc.

# Session
Guarda informacao em relacao ao cliente do lado do servidor. Presicamos de identificadors para o fazer. Existem pacotes para o fazer. Um exemplo é o modulo **uuid**. Pode ser pervo timestamp(v1), namespace(v2) e random(v4).

~~~
npm i express-session --save
npm insatall uuid --save
~~~
Para persistir os IDs de sessao:
~~~
npm i session-file-store --save
~~~
Temos de configurar este pacote. Para o fazer, temos de meter código.

# +Coisas

Dentro do get, podemos ver:
~~~
console.log(req.sessionID)
~~~

De lembrar que se fizermos 2 pedidos em browsers diferentes, ele cria 2 IDs.

# Autenticao
~~~
npm i passport passport-local --save
~~~
Esta maneira só associa nome e palavra-passe.


# Infos nada relacionadas
Se mandamos uma RAW tem de ser mandado em formato JSON.