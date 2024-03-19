var mongoose = require('mongoose')
const {modelName}=require('../models/alunos')
var Aluno = require('../models/alunos')

//Get
module.exports.list=()=>{
    return Aluno.find().sort({nome:1}).exec()
}

//Insert
module.exports.insert=aluno=>{
    var newAluno=new Aluno(aluno)
    return newAluno.save()
}

//Update
module.exports.list=(id,aluno)=>{
    return Aluno.findByIdAndUpdate(id,aluno,{new:true}).exec() //new é para devolver os dados que foram mudados
}

//Delete
module.exports.remove=id=>{
    return Aluno.findByIdAndDelete(id).exec()

    //ALTERNATIVA QUE FUNCIONA
    //Aluno.find({_id:id}).deleteOne().exec()
}
