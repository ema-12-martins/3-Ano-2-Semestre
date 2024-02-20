Ir para a diretoria:

Para correr a bd:
json-server --watch db.json
Para correr o servidor:
node servidor.js

Teem de estar a correr em portas diferentes parque que nao haja problemas

Testes:
http://localhost:3000/lista
http://localhost:3000/lista?_sort=nome
http://localhost:3000/lista?quantidade=2

...................................................
Lista cidades ordenadas por nome:
3000/cidades?_sort=nome

Lista cidades do destrito ordenadas por nome:
3000/cidades?_sort=nome&distrito=Braga

Ligacoes com origem c1:
ligacoes?origem=c1

Ligacoes com destino em c10:
ligacoes?destino=c10


Colocar json server a correr sobre dataset da escola de musica e fazer uma pagina web em nodejs. Ir buscar as infos ao dataset e criar uma apgina. A pagina tem de ter indice, pagina de instrumentos, indice.