var express = require('express');
var router = express.Router();

var jsonfile = require('jsonfile')
var fs = require('fs')
var multer = require('multer')
var upload = multer ({dest:'uploads'})


router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/files', upload.single('myFile'), (req,res) =>{
  console.log('cdir: '+__dirname);
  let oldPath = __dirname + '/../' + req.file.path
  console.log(oldPath)
  let newPath = __dirname +'/../public/fileStore/' + req.file.originalname
  console.log(newPath)
  
  fs.rename(oldPath,newPath, err =>{ /*Moder o ficheiro da pasta antiga para a nova */
    if(err) throw err
  })

  var date = new Date().toISOString().substring(0,19)
  var files = jsonfile.readFileSync(__dirname+'/../data/dbFiles.json')

  files.push({
    date: date,
    name: req.file.originalname,
    mimetype: req.file.mimetype,
    size: req.file.size
  })

  jsonfile.writeFileSync(__dirname+'/../data/dbFiles.json',files)

  res.redirect('/')
})

module.exports = router;
