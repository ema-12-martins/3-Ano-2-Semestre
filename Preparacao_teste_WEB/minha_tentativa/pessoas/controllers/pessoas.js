const mongoose = require('mongoose')
var Pessoas = require("../models/pessoas")

module.exports.list = () => {
    return Pessoas
        .find()
        .exec()
}


module.exports.insert = pess => {
    if((Pessoas.find({_id : pess._id}).exec()).length != 1){
        var newPessoa = new Pessoas(pess)
        return newPessoa.save()
    }
}