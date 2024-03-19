# abrir SH do MONGO
~~~
docker start 34a3ad5c07d
docker exec -it mongoEW bash
mongosh
~~~

# Mandar ficheiro json para criar uma nova BD
~~~
docker cp <nome> mongoEW:/tmp
docker exec -it mongoEW bash
mongoimport -d tp2ew2024 -c atletas /tmp/<nome>
~~~
Se for um array, o comando anterior passa a ser:
~~~
mongoimport -d tp2ew2024 -c alunos /tmp/alunos.json --jsonArray
~~~

# Comandos interessantes
Mostrar as bds:
~~~
show dbs
~~~
Usar uma bd:
~~~
use <nome>
~~~
Mostrar as colecoes:
~~~
show collections
~~~

# Exercicios com a bd dos atletas
Procurar todos os atletas (it para ver mais):
~~~
db.atletas.find() 
~~~

Retornar o nome e morada dos atletas:
~~~
db.atletas.find({},{_id:0,nome:1,morada:1})
~~~

Quanto atletas em cada prova:
~~~
bd.atletas.agregate([
	{
	$group:{_id:"$prova",total:{$sum:1}}
	}
])
~~~

Quantos atletas femininos inscritos na corrida ultra:
~~~
db.atletas.countDocuments({prova:/Ultra/,escalao:/Fem/})
~~~

Listar o nome e data de nasciemnto da equipa turbulentos:
~~~
db.atletas.find({equipa:/turbulentos/i},{_id:0,nome:1,dataNasc:1})
~~~

# Gerar com o npx uma aplicação express
Este exemplo é para criar a plicação chamada apiAlunos
~~~
npx express-generator apiAlunos
cd apiAlunos
npm install -i
npm install mongoose
npm start
~~~