const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
  last_login: {
    type: Date,
    default: Date.now,
  },
  type: {
    type: String,
    default: "Trial",
  },
  sync: {
    const_data: {
      type: String,
      default: "0",
    },
    config: {
      type: String,
      default: "0",
    },
  },
});

const User = mongoose.model("User", UserSchema);

module.exports = User;
