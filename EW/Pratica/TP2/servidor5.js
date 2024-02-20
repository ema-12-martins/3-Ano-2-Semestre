var http = require('http')
var url = require('url')
var axios=require('axios') //Fazer pedidos a api de dados

http.createServer((req,res) =>{
    res.writeHead(200,{'Content-Type':'text/html; charset=utf-8'})

    if(req.url=="/cidades"){
        axios.get("http://localhost:3000/cidades?_sort=nome") //Ordenados por nome
        .then((resp)=>{
            var data=resp.data

            res.write("<ul>")
            for (i in data){
                res.write("<li><a href='/cidades/"+data[i].id+"'>"+data[i].nome"</a></li>")
            }
            res.write("</ul>")
        })
        .catch((erro)=>{
            console.log("Erro: "+erro)
            res.write("<p>"+erro+"</pre>")
        })
        res.end() //Temos de fazer aqui pois temos espacos de enderecamentos diferentes (temos um copia do objeto res)
    }else if(req.url.match(/\/cidades\/c\d+/)){
        let id=req.url.substring(9) //Para obtermos o id
        axios.get("http://localhost:3000/cidades?_sort=nome") //Ordenados por nome
        .then((resp)=>{
            var data=resp.data

            res.write("<h1>"+data.nome+"</h1>")
            res.write("<h3>"+data.distrito+"</h3>")
            res.write("<b>Populacao: </b>"+data["populacao"]) //Se tiver acentos, temos de colocar assim
            res.write("<br>")
            res.write(data["descrição"])
            res.write("<h6><a href='/cidades'>Voltar</a></h6>")
        })
        .catch((erro)=>{
            console.log("Erro: "+erro)
            res.write("<p>"+erro+"</pre>")
        })
        res.end()


        
    }else{
        res.write("Operacao nao suportada")
        res.end()
    }

}).listen(2007)

console.log("Servidor à escuta na porta 2007");