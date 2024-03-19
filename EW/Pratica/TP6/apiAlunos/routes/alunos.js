var express = require('express');
var router = express.Router();
var Aluno = require('../controllers/alunos')

/* GET users listing. */
router.get('/', function(req, res, next) {
  Aluno.list()
    .then(data=>{
      res.jsonp(data)
    })
    .catch(e => res.jsonp(e))
});

router.post('/', function(req, res, next) {
  Aluno.insert(req.body)
    .then(data=>{
      res.jsonp(data)
    })
    .catch(e => res.jsonp(e))
});

router.put('/:id', function(req, res, next) {
  Aluno.update(req.params.dictionary,req.body)
    .then(data=>{
      res.jsonp(data)
    })
    .catch(e => res.jsonp(e))
});

router.delete('/:id', function(req, res, next) {
  Aluno.remove(req.params.dictionary,req.body)
    .then(data=>{
      res.jsonp(data)
    })
    .catch(e => res.jsonp(e))
});





module.exports = router;
