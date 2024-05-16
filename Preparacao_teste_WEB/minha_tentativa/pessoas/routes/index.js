
var express = require('express');
var router = express.Router();
var Pessoas = require('../controllers/pessoas')
var multer = require('multer')
const upload = multer({ dest: 'uploads/' })
var fs = require('fs')
   
/* GET home page. */
router.get('/', function(req, res, next) {
  Pessoas.list()
      .then(data => res.jsonp(data))
      .catch(erro => res.jsonp(erro))
});

router.post('/', upload.single('foto'), function(req, res){
  var pessoa={
    _id : req.body._id, //Datas->creationDate: new Date()
    nome: req.body.nome,
    foto:'foto.' + req.file.originalname.split('.')[1]
  }
  Pessoas.insert(pessoa)
    .then(data => {
      fs.mkdir( __dirname + "/../FileStore/" + pessoa._id, { recursive: true }, (err) => {
        if (err) {
          console.error('Error creating folder:', err);
        } else {
          let oldPath = __dirname + '/../' + req.file.path 
          let newPath = __dirname + '/../FileStore/' + pessoa._id + '/foto.' + req.file.mimetype.split('/')[1] 
          fs.rename(oldPath, newPath, function(error){
            if(error) throw error
            res.jsonp(data); // Moveu isso aqui para dentro do else
          })
        }
      });
    })
    .catch(erro => res.jsonp(erro))
});

module.exports = router;
