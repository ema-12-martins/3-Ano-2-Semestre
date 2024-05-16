var express = require('express');
var router = express.Router();
var Contracts = require('../controllers/contracts')

/* GET users listing. */
router.get('/', function(req, res) {
  const year = req.query.year;
  if(!year){
    Contracts.findContratosAno(req.query.year)
    .then(data => res.jsonp(data))
    .catch(erro => res.jsonp(erro))
  }else{
    Contracts.list()
    .then(data => res.jsonp(data))
    .catch(erro => {
      console.log(erro)
      res.jsonp(erro)
    })
  }
});

router.get('/:id', function(req, res) {
  if(req.params.id==='courses'){
    Contracts.cursosContratados()
    .then(data => res.jsonp(data))
    .catch(erro => res.jsonp(erro))
  }else{
    Contracts.findById(req.params.id)
    .then(data => res.jsonp(data))
    .catch(erro => res.jsonp(erro))
  }
});


module.exports = router;
