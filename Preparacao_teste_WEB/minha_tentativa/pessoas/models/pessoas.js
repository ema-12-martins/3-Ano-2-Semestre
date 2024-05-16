var mongoose = require("mongoose")

var pessoasSchema = new mongoose.Schema({
    _id : String, 
    nome: String,
    foto: String, //path para ficheiro

}, { versionKey: false })

module.exports = mongoose.model('pessoas', pessoasSchema)