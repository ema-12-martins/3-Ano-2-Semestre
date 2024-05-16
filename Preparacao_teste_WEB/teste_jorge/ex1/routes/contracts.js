var express = require('express');
var router = express.Router();
var Contracts = require('../controllers/contracts');
const contracts = require('../models/contracts');

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

/* Criar uma UC (C) */
router.post('/', function(req, res) {
  console.log(req.body)
  Contracts.insert(req.body)
    .then(data => res.status(201).jsonp(data))
    .catch(erro => res.jsonp(erro))
});

/*Se for com form o post é diferente */
  /* router.post('/', upload.single('enunciado'), function(req, res){
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
 */

/* Remover uma Entrega (D ) */
router.delete('/:id', function(req, res) {
  Contracts.remove(req.params.id)
    .then(removedContract => {
      if (!removedContract) {
        return res.status(404).jsonp({ error: 'Contract not found' });
      }
      res.jsonp(removedContract);
    })
    .catch(error => res.status(500).jsonp(error));
});

module.exports = router;
