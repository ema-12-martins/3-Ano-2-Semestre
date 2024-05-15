var express = require('express');
var router = express.Router();
var Contracts = require('../controllers/contracts')

/* GET users listing. */
router.get('/', function(req, res) {
  Contracts.list()
    .then(data => res.jsonp(data))
    .catch(erro => {
      console.log(erro)
      res.jsonp(erro)
    })
});

router.get('/:id', function(req, res) {
  Contracts.findById(req.params.id)
    .then(data => res.jsonp(data))
    .catch(erro => res.jsonp(erro))
});

module.exports = router;
