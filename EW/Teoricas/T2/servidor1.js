//Carregar modolus
var http=require('http');

http.createServer(function(req,res){ //Qando estiver pronto, realiza a funcao anonima que tem a request e a response
    res.writeHead(200,{'Content-Type':'text/html; charset=utf-8'}); //200-sucesso. A menssagem de resposta é de texto (plain para testo e html para html)
    console.dir(req) //Permite ver uma estrutura de dados completa
    res.write('<h1>Olá turma de 2024!</h1>');
    res.write(req.url);
    res.end();
}).listen(7777); //Vais estar a escuta na porta 7777