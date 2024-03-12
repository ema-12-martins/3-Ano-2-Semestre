var express = require('express');
var router = express.Router();

/* Redireciona para outra pagina. */
router.get('/', function(req, res, next) {
  res.redirect("/alunos")
});

module.exports = router;
