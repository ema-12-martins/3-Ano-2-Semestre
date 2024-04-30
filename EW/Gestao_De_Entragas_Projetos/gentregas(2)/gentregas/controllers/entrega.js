const mongoose = require('mongoose')
var Entrega = require("../models/entrega")

module.exports.list = () => {
    return Entrega
        .find()
        .sort({creationDate : 1})
        .exec()
}

module.exports.findById = id => {
    return Entrega
        .findOne({_id : id})
        .exec()
}

module.exports.findByEquipa = id => {
    return Equipa
        .find({idEq : idEquipa})
        .sort({creationDate : 1})
        .exec()
}

module.exports.insert = ent => {
    if((Entrega.find({_id : ent._id}).exec()).length != 1){
        var newEntrega = new Entrega(ent)
        return newEntrega.save()
    }
}

module.exports.findByUc = idUc => {
    return Entrega
        .findOne({uc : idUc}) //model, variavel
        .sort({creationDate : 1})
        .exec()
}

module.exports.findByProjeto = idProjeto => {
    return Entrega
        .findOne({idProj : idProjeto}) //model, variavel
        .sort({creationDate : 1})
        .exec()
}

module.exports.countByProjeto = idProjeto => {
    return Entrega
        .countDocuments({idProj : idProjeto}) //model, variavel
        .exec()
}

module.exports.update = (id, ent) => {
    return Entrega
        .findByIdAndUpdate(id, ent, {new : true})
        .exec()
}

module.exports.remove = id => {
    Entrega
        .find({_id : id})
        .deleteOne()
        .exec()
}

module.exports.remove = id => {
    return Entrega
        .findByIdAndDelete({_id : id})
        .exec()
}