# Fazer o import para o mongo DB
**NAO ESQUECER METER IDS**

Nos seguintes comandos o **nome** corresponde ao nome do ficheiro que queremos importar.
Para colocar a BD no mongo, temos de seguir os seguintes passos:
~~~
docker start 34a3ad5c07d
docker cp <nome> mongoEW:/tmp
docker exec -it mongoEW bash
mongoimport -d <nome_bd> -c <nome_colection> /tmp/<nome>
~~~
Se for um array, temos de adicionar uma flag
~~~
mongoimport -d <nome_bd> -c <nome_colection> /tmp/<nome> --jsonArray
~~~
Para correr para testar de está tudo a funcionar:
~~~
docker exec -it mongoEW bash
mongosh
show dbs
use <nome_bd>
~~~

# Comandos exemplo de como usar o mongo
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
V
Quantos atletas femininos inscritos na corrida ultra:
~~~
db.atletas.countDocuments({prova:/Ultra/,escalao:/Fem/})
~~~

Listar o nome e data de nasciemnto da equipa turbulentos:
~~~
db.atletas.find({equipa:/turbulentos/i},{_id:0,nome:1,dataNasc:1})
~~~

# Montar a APP com npx
~~~
npx express-generator <\nome> --view=pug
cd <\nome>
npm install
npm install jsonfile
npm install multer
npm install -i
npm install mongoose
npm start
~~~

Para a pasta javascripts:
1. https://code.jquery.com/jquery-3.7.1.min.js
2. https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.2/jquery.modal.min.js

Para a pasta stylesheet:
1. https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.2/jquery.modal.css
2. https://www.w3schools.com/w3css/4/w3.css

Dentro da **public** criar a pasta **fileStore**. Dentro dos scripts, meter os 2 ficheiros anteriores. Na pasta stylesheets meter os outros 2 links.

Iniciamos o ficheiro db.Files.json com uma [].

Criar pasta com o models e depois o controllers.
