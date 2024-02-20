var http = require('http')
var url = require('url')

http.createServer((req,res) =>{
    console.log(req.method+""+req.url)
    res.writeHead(200,{'Content-Type':'text/html; charset=utf-8'})
    
    var q = url.parse(req.url,true)

    if(q.pathname=="/add"){
        var n1=parseInt(q.query.n1,10)
        var n2=parseInt(q.query.n2,10)
        var soma=n1+n2
        res.write("<pre>"+n1+ "+"+n2+"="+soma+"</pre>")
    }else if (q.pathname=="/sub"){
        var n1=parseInt(q.query.n1,10)
        var n2=parseInt(q.query.n2,10)
        var sub=n1-n2
        res.write("<pre>"+n1+ "-"+n2+"="+sub+"</pre>")

    }else{
        res.write("Operacao nao suportada")
    }


    res.end()
}).listen(2005)

console.log("Servidor à escuta na porta 2005");