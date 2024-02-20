var http = require('http')

http.createServer((req,res) =>{
    res.writeHead(200,{'Content-Type':'text/plain; charset=utf-8'})
    res.end('Olá mundo! Turma de Eng Web 2024 Turno 3.')
}).listen(2002)

console.log("Servidor à escuta na porta 2002");