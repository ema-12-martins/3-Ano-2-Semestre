# Base para um servidor web

Fazer **GET** ou seja, ir buscar dados à BD.
~~~
const axios = require('axios');

axios.get('http://localhost:3000/alunos')
    .then(resp => {
        data = resp.data;
        data.forEach(a => {
            console.log(JSON.stringify(data)); // Passa o objeto para string
        });
    })
    .catch(error => {
        console.log(error);
    });
~~~

Para colocar um objeto usamos o **POST**.
~~~
const axios = require('axios');

axios.post('http://localhost:3000/instrumentos',{
    "id": "I23",
    "#text": "Castanholas"
}).then(resp => {
    console.log(resp.data);
}).catch(error => {
    console.log(error);
});
~~~

Para alterar um registo usar o **PUT**.
~~~
const axios = require('axios');

axios.put('http://localhost:3000/alunos/101',{
    "id": "a101"
}).then(resp => {
    console.log(resp.data);
}).catch(error => {
    console.log(error);
});
~~~

Para apagar dados, fazer o **DELETE**.
~~~
const axios = require('axios');
axios.delete('http://localhost:3000/alunos/101',{
}).then(resp => {
    console.log(resp.data);
}).catch(error => {
    console.log(error);
});
~~~

---

Se queremos depois de fazer um pedido responder com um ficheiro, fazemos o seguinte:

~~~
var http = require('http');
var fs = require('fs'); //Para ficheiros

http.createServer(function (req, res) {

    //Para saber os pedidos que sao feitos
    van date=new Date().toString().substring(0,16); //Da a data e horas
    console.write(req.method+" "+req.url+" "+date);

    //Para escrever os pedidos propriamente ditos
    fs.readFile('pag1.html', function (erro, dados) {
        if (!erro){
            res.writeHead(200, {'Content-Type': 'text/html;charset=utf-8'});
            res.write(dados);
            res.end();
        }else{
            res.write("<pre>" + erro + "</pre>");
            res.end();
        }
    });
}).listen(8080); 

~~~

Como não especificamos a rota, todas elas vão ficar com o texto da pag1.html.

---

Temos de notar que:
- **req.method** retorna o método (POST,GET...)
- **req.url** retorna o URL
- Para irmos subscar uma parte do URL do pedido **url.parse(req.url,true).pathname.substring(num);**

Podemos usar regex para determinar o que temos de exibir na página.