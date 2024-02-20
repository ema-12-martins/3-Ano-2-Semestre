var http = require('http')
var meta = require('./aux')
var url = require('url')

http.createServer((req,res) =>{
    console.log(req.method+""+req.url)
    res.writeHead(200,{'Content-Type':'text/html; charset=utf-8'})
    res.write("<h1>Uma página Web</h1>")
    
    var q1 = url.parse(req.url,true)
    res.write("TRUE: <pre>"+JSON.stringify(q1)+"</pre>")

    var q2 = url.parse(req.url,false)
    res.write("FALSE: <pre>"+JSON.stringify(q2)+"</pre>")

    res.end()
}).listen(2004)

console.log("Servidor à escuta na porta 2004");