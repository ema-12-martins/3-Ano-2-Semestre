const mongoose = require('mongoose')
var Equipa = require("../models/equipa")

module.exports.list = () => {
    return Equipa
        .find()
        .sort({designacao : 1})
        .exec()
}

module.exports.findById = id => {
    return Equipa
        .findOne({_id : id})
        .exec()
}

module.exports.insert = eq => {
    if((Equipa.find({_id : eq._id}).exec()).length != 1){
        var newEquipa = new Equipa(eq)
        return newEquipa.save()
    }
}

module.exports.update = (id, eq) => {
    return Equipa
        .findByIdAndUpdate(id, eq, {new : true})
        .exec()
}

module.exports.remove = id => {
    Equipa
        .find({_id : id})
        .deleteOne()
        .exec()
}