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
