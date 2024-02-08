const mongoose = require("mongoose");

const EventSchema = new mongoose.Schema({
  user: {
    type: String,
    required: true,
  },
  origin: {
    type: String,
    required: true,
  },
  msg: {
    type: String,
    required: true,
  },
  timestamp: {
    type: Number,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
  target: {
    type: String,
    required: false,
  },
});

const Event = mongoose.model("Event", EventSchema);

module.exports = Event;
