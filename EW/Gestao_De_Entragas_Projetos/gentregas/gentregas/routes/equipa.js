/* Operações CRUD sobre Equipa 
   2024-04-21 @jcr
   ----------------------- */
var express = require('express');
var router = express.Router();
var Equipa = require('../controllers/equipa')
var Entrega = require('../controllers/entrega')

/* Listar as Equipa (R) */
router.get('/', function(req, res) {
    Equipa.list()
        .then(data => res.jsonp(data))
        .catch(erro => res.jsonp(erro))
});

/* Consultar uma Equipa (R) */
router.get('/:id', function(req, res) {
    Equipa.findById(req.params.id)
      .then(data => res.jsonp(data))
      .catch(erro => res.jsonp(erro))
  });

/* Criar uma Equipa (C) */
router.post('/', function(req, res) {
  Equipa.insert(req.body)
    .then(data => res.jsonp(data))
    .catch(erro => res.jsonp(erro))
});

/* Alterar uma Equipa (U) */
router.put('/:id', function(req, res) {
  Entrega.findByEquipa(req.params.id)
    .then(listaEntregas => {
      if(listaEntregas.lenght == 0){
        Equipa.update(req.params.id, req.body)
        .then(data => res.jsonp(data))
        .catch(erro => res.jsonp(erro))
      }
    })
    .catch(erro => res.jsonp(erro))
   
  });


/* Alterar uma Equipa (U) */
router.delete('/:id', function(req, res) {
  Entrega.findByEquipa(req.params.id)
    .then(listaEntregas => {
      if(listaEntregas.lenght == 0){
        Equipa.remove(req.params.id, req.body)
        .then(data => res.jsonp(data))
        .catch(erro => res.jsonp(erro))
      }
    })
    .catch(erro => res.jsonp(erro))
   
  });


/* Remover uma Equipa (D ) */
router.delete('/:id', function(req, res) {
    return Equipa.remove(req.params.id)
      .then(console.log("Deleted " + req.params.id))
      .catch(erro => res.jsonp(erro))
  });

module.exports = router;
