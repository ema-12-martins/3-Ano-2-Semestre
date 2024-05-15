const mongoose = require('mongoose')
var Contracts = require("../models/contracts")

module.exports.list = () => {
    return Contracts
        .find()
        .sort({creationDate : 1})
        .exec()
}
