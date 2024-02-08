const mongoose = require("mongoose");

const ConstantDataSchema = new mongoose.Schema({
  user: {
    type: String,
    required: true,
  },
  node: {
    type: String,
    required: true,
  },
  data: {
    type: String,
    required: true,
  },
});

const ConstantData = mongoose.model("ConstantData", ConstantDataSchema);

module.exports = ConstantData;
