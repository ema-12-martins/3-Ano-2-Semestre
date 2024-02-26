var http = require('http');
var fs = require('fs'); //Para ficheiros

http.createServer(function (req, res) {
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

