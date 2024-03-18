# O que é o Docker
Esta por cima do SO. Podemos ter vários containers que podem ter aplicacoes. Uma imagem é um conjunto de bits com algo la dentro. Um container é essa imagem já pronta, as vezes até já a ser executadas.

~~~
docker build -t jcr/node-web-app-hello

docker images //ver as imagens que tenho

docker run -d -p 3000:7777 --name hello ID_imagem //Para correr a imagem.

docker logs hello

docker ps //lista de containers a correr na maquina

docker stop hello //para o container

docker rm hello //remover os recursos que o container esta a utilizar

docker pull mongo //vai buscar um container

docker exec -it mongoEW mongosh//Interpretador do mongo

~~~

Para o mongo db, o porta interna default é a 27017.
No doecker run, ao fazer 3000:7777 estamos a passar a porta interna 7777 para a porta externa 3000. O argumento seguinte ocrresponde ao id em hexadecimal.
O it no exec é para ter o input

# Mongo
Dentro do mongo:
~~~
show dbs //Diz quais sao as bd dentro do mongo
~~~
Dentro do mongo trabalha-se com json.Tem de ter uma estrutura especifica. Temps duas hipoteses. A primeira é um objeto por linha.
~~~
{
    "id":"A12883",
    "nome":"Jose",
}
~~~
A outra forma é uma lista de dicionários.
~~~
[
    {
        "id":"A12883",
        "nome":"Jose",
    },
    {
        "id":"A12883",
        "nome":"Jose",
    }
]
~~~

Para sair do mongo shell:
~~~
quit()
~~~

Para importar a bd:
~~~
docker cp  <nome do ficheiro> mongoEW:/tmp //copia do meu sistema para o container para a pasta temporaria
docker exec -it mongoEW bash //
~~~

Agora na bash:
~~~
mongoimport -d pubs -c pubs /tmp/jcrpubs.json --jsonArray //Para termos a pubs chamda pubs
~~~

Para usar a bd:
~~~
use pubs

db.pubs.find //da todos os registos

db.pubs.findOne().pretty //print de 1 registo

db.pubs.countDocuments() //Da o numero de registos da colecao

db.push.find({year:"2011"}) //Filtro de select

db.push.find({year:"2011"}).countDocuments() //Conta quantos registos em 2011.

db.pubs({year:{$gte:"2011"}}) //Maior ou igual a 2011

db.push.find({year:"2011"}).countDocuments() //Conta quantos registos em 2011.

db.push.find({year:"2011"},{title:1,_id=0}).sort({title:-1}) //Projecoes

db.pubs.find({},{title:1,_id:0,type:1}).sort({title:1,year:-1})//Farios criterios de ordenacao.


db.pubs.aggregate([
    {"$unwind":"$authors"},
    {"$match":{"autors":"José Carlos Ramalho"}},
    {"$group":{"_id":"$year","count":{"$sum":1}}},
    {"$sort":{"_id":-1}}
])

db.pubs.insertOne({_id:"xyz123",comida:"parta italiana"})
~~~
Por omissao, _id esta a 1 e o resto está a 0. Nas projecoes temos de dizer o que queremos por a 1 para que apareça.
O unwith se tivermos uma lista, replica em varios registos.

# TPC 
- Carregar dataset para mongo bd.
- Usar express para usar uma api rest. Recebe pedidos HTTP e responde com JSON.
- Se precisar de dados, pede ao mongo para o fazer.
- Pagina web com interfaces.