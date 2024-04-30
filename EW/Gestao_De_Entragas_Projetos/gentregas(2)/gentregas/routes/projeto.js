/* Operações CRUD sobre Equipa 
   2024-04-21 @jcr
   ----------------------- */
   var express = require('express');
   var router = express.Router();
   var Projeto = require('../controllers/projeto')
   var Entrega = require('../controllers/entrega')
   var multer = require('multer')
   const upload = multer({ dest: 'uploads/' })
   var fs = require('fs')
   
   /* Listar as Projeto (R) */
   router.get('/', function(req, res) {
    if(req.query.uc){
        Projeto.findByIdUC(req.query.uc)
           .then(data => res.jsonp(data))
           .catch(erro => res.jsonp(erro))
    }else{
        Projeto.list()
           .then(data => res.jsonp(data))
           .catch(erro => res.jsonp(erro))
    }
       
   });
   
   /* Consultar uma Projeto (R) */
   router.get('/:id', function(req, res) {
       Projeto.findById(req.params.id)
         .then(proj => {
            Entrega.countByProjeto(proj._id)
              .then(nEntregas => {
                proj["n_entregas"] = nEntregas
                res.jsonp(proj)
              })
              .catch(erro =>res.jsonp(erro))
         })
         .catch(erro => res.jsonp(erro))
     });
   
   /* Criar uma Projeto (C) */
   router.post('/', upload.single('enunciado'), function(req, res){
      var projeto={
        _id : req.body._id, 
        creationDate: new Date(),
        limitDate: req.body.limitDate,
        anoLetivo: req.body.anoLetivo,
        uc: req.body.uc,
        designacao: req.body.designacao,
        resumo:req.body.resumo,
        enunciado:'enunciado.' + req.file.originalname.split('.')[1]
      }
     Projeto.insert(projeto)
       .then(data => {
        fs.mkdir( __dirname + "/../FileStore/" + projeto._id, { recursive: true }, (err) => {
          if (err) {
            console.error('Error creating folder:', err);
          } else {
            for(let i=0; i < req.files.length; i++){
              let oldPath = __dirname + '/../' + req.files.path 
              let newPath = __dirname + '/../FileStore/' + projeto._id + '/enunciado.' + (i+1) + req.files.originalname.split('.')[1]
              fs.rename(oldPath, newPath, function(error){
                if(error) throw error
              })
            }
          }
        res.jsonp(data)
       })
       .catch(erro => res.jsonp(erro))
   });
  }
   
   /* Alterar uma Projeto (U) */
   router.put('/:id', function(req, res) {
      Entrega.countByProjeto(req.paramens.id)
        .then(nEntregas => {
          if(nEntregas == 0){
            Projeto.update(req.params.id, req.body)
                    .then(data => res.jsonp(data))
                    .catch(erro => res.jsonp(erro))
          }
        }).catch(erro => res.jsonp(erro))
     });
   
   
   /* Alterar uma Projeto (U) */
   router.delete('/:id', function(req, res) {
    Entrega.countByProjeto(req.paramens.id)
      .then(nEntregas => {
        if(nEntregas == 0){
          Projeto.remove(req.params.id, req.body)
                  .then(data => res.jsonp(data))
                  .catch(erro => res.jsonp(erro))
        }
      }).catch(erro => res.jsonp(erro))
   });
   
   module.exports = router;
   