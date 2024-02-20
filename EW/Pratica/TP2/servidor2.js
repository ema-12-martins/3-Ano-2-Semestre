var http = require('http')
var meta = require('./aux')

http.createServer((req,res) =>{
    console.log(req.method+""+req.url)
    res.writeHead(200,{'Content-Type':'text/html; charset=utf-8'})
    res.write("<h1>Uma página Web</h1>")
    res.write("<p>Página criaca com node.js por"
    +meta.myName()
    +"em"
    +meta.myDateTime()
    +"na turma"
    + meta.myTurma
    +"</p>")
    res.end()
}).listen(2003)

console.log("Servidor à escuta na porta 2003");