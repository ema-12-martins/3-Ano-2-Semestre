const mongoose = require('mongoose')
var Contracts = require("../models/contracts")

module.exports.list = () => {
    return Contracts
        .find()
        .sort({creationDate : 1})
        .exec()
}

module.exports.findById = id => {
    return Contracts
        .findOne({_id : id})
        .exec()
}

module.exports.findContratosAno = ano => {
    return Contracts.find({
        $and: [
            { DataInicioContrato: { $lte: `31/12/${ano}` } },
            { DataFimContrato: { $gte: `01/01/${ano}` } }
        ]
    }).exec();
}

module.exports.cursosContratados = () => {
    return Contracts
        .distinct("Curso")
        .exec()
}

module.exports.insert = con => {
    if((Contracts.find({_id : con._id}).exec()).length != 1){
        var newContracts = new Contracts(con)
        return newContracts.save()
    }
}

module.exports.remove = id => {
    return Contracts
        .find({_id : id})
        .deleteOne()
        .exec()
}

module.exports.update = (id, cont) => {
    return Contracts
        .findByIdAndUpdate(id, cont, {new : true})
        .exec()
}
