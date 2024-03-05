// alunos_server.js
// EW2024 : 04/03/2024
// by jcr

var http = require('http')
var axios = require('axios')
const { parse } = require('querystring');

var templates = require('./templates')          // Necessario criar e colocar na mesma pasta
var static = require('./static.js')             // Colocar na mesma pasta

// Aux functions
function collectRequestBodyData(request, callback) {
    if(request.headers['content-type'] === 'application/x-www-form-urlencoded') {
        let body = '';
        request.on('data', chunk => {
            body += chunk.toString();
        });
        request.on('end', () => {
            callback(parse(body));
        });
    }
    else {
        callback(null);
    }
}

// Server creation

var alunosServer = http.createServer((req, res) => {
    // Logger: what was requested and when it was requested
    var d = new Date().toISOString().substring(0, 16)
    console.log(req.method + " " + req.url + " " + d)

    // Handling request
    if(static.staticResource(req)){
        static.serveStaticResource(req, res)
    }
    else{
        switch(req.method){
            case "GET": 
                // GET /alunos --------------------------------------------------------------------
                if(req.url=="/" || req.url=="/alunos"){
                    axios.get("http://localhost:3000/alunos?_sort=nome")
                        .then(resp=>{
                            alunos=resp.data
                            res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'})
                            res.write(templates.studentsListPage(alunos,d))
                            res.end()

                        })
                        .catch(erro=>{
                            res.writeHead(503,{'Content-Type':'text/html;charset=utf-8'})
                            res.write("<p>Nao foi possivel obter a lista de alunos: "+erro+"</p>")
                            res.end()
                        })
                }
                // GET /alunos/:id --------------------------------------------------------------------
                else if(/\/alunos\/(A|PG)[0-9]+$/i.test(req.url)){ //i par nao ligar ao case
                    id = req.url.split('/')[2]
                    axios.get("http://localhost:3000/alunos/"+id)
                        .then(resp=>{
                            aluno=resp.data
                            res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'})
                            res.write(templates.studentPage(aluno,d))
                            res.end()

                        })
                        .catch(erro=>{
                            res.writeHead(504,{'Content-Type':'text/html;charset=utf-8'})
                            res.write("<p>Nao foi possivel obter a informação do aluno"+id+":"+erro+"</p>")
                            res.end()
                        })
                }
                // GET /alunos/registo --------------------------------------------------------------------
                else if(req.url=="/alunos/registo"){
                    res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'})
                    res.write(templates.studentFormPage(d))
                    res.end()

                }
               
                // GET /alunos/edit/:id --------------------------------------------------------------------
                else if(/\/alunos\/edit\/(A|PG)[0-9]+$/i.test(req.url)){
                    id = req.url.split('/')[3]
                    axios.get("http://localhost:3000/alunos/"+id)
                        .then(resp=>{
                            aluno=resp.data
                            res.writeHead(201,{'Content-Type':'text/html;charset=utf-8'})
                            res.write(templates.studentFormEditPage(aluno,d))
                            res.end()

                        })
                        .catch(erro=>{
                            res.writeHead(505,{'Content-Type':'text/html;charset=utf-8'})
                            res.write("<p>Nao foi possivel obter a informação do aluno"+id+":"+erro+"</p>")
                            res.end()
                        })
                }
               
                // GET /alunos/delete/:id --------------------------------------------------------------------
                else if(/\/alunos\/delete\/(A|PG)[0-9]+$/i.test(req.url)){
                    id = req.url.split('/')[3]
                    axios.delete("http://localhost:3000/alunos/"+id)
                        .then(resp=>{
                            res.writeHead(201,{'Content-Type':'text/html;charset=utf-8'})
                            res.write("<p>Registo Apagado</p>")
                            res.end()

                        })
                        .catch(erro=>{
                            res.writeHead(510,{'Content-Type':'text/html;charset=utf-8'})
                            res.write("<p>Nao foi possivel eliminar o aluno "+id+":"+erro+"</p>")
                            res.end()
                        })
                }
                
                // GET ? -> Lancar um erro
                else{
                    res.writeHead(502,{'Content-Type':'text/html;charset=utf-8'})
                    res.write("<p>Get request não suportado:"+req.url+"</p>")
                    res.end()
                }
                break
            case "POST":
                // POST /alunos/registo --------------------------------------------------------------------
                if(req.url=="/alunos/registo"){
                    collectRequestBodyData(req,result=>{
                        if(result){
                            console.log(result)
                            axios.post("http://localhost:3000/alunos",result)
                                .then(resp=>{
                                    res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'})
                                    res.write("<pre>Registo inserido:"+JSON.stringify(resp.data)+"</pre>")
                                    res.end()
                                })
                                .catch(erro=>{
                                    res.writeHead(507,{'Content-Type':'text/html;charset=utf-8'})
                                    res.write(templates.errorPage("Não foi possivel adicionar...",d))
                                    res.end()
                                })
    
                        }else{
                            res.writeHead(509,{'Content-Type':'text/html;charset=utf-8'})
                                res.write("<p>Nao foi possivel obter os dados dobody</p>")
                                res.end()
                        }
                    }) 
                }
                
                // POST /alunos/edit/:id --------------------------------------------------------------------
                else if(/\/alunos\/edit\/(A|PG)[0-9]+$/i.test(req.url)){
                    //Vai buscar os dados ao body
                    collectRequestBodyData(req,result=>{
                        if(result){
                            console.log(result)
                            axios.put("http://localhost:3000/alunos/"+result.id,result)
                                .then(resp=>{
                                    res.writeHead(200,{'Content-Type':'text/html;charset=utf-8'})
                                    res.write("<pre>Registo alterado:"+JSON.stringify(resp.data)+"</pre>")
                                    res.end()
                                })
                                .catch(erro=>{
                                    res.writeHead(507,{'Content-Type':'text/html;charset=utf-8'})
                                    res.write(templates.errorPage("Não foi possivel editar...",d))
                                    res.end()
                                })
    
                        }else{
                            res.writeHead(506,{'Content-Type':'text/html;charset=utf-8'})
                                res.write("<p>Nao foi possivel obter os dados dobody</p>")
                                res.end()
                        }
                    }) 
                }

                // POST ? -> Lancar um erro
                else{
                    res.writeHead(501,{'Content-Type':'text/html;charset=utf-8'})
                    res.write("<p>Post request não suportado:"+req.url+"</p>")
                    res.end()
                }
                break
            default: 
                // Outros metodos nao sao suportados
                res.writeHead(500,{'Content-Type':'text/html;charset=utf-8'})
                res.write("<p>Método nao suportado:"+req.method+"</p>")
                res.end()
                break
        }
    }
})

alunosServer.listen(3050, ()=>{
    console.log("Servidor à escuta na porta 3035...")
})



