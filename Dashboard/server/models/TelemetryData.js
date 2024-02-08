const mongoose = require("mongoose");

const TelemetryDataSchema = new mongoose.Schema({
  user: {
    type: String,
    required: true,
  },
  node: {
    type: String,
    required: true,
  },
  timestamp: {
    type: Number,
    required: true,
  },
  data: {
    type: String,
    required: true,
  },
});

const TelemetryData = mongoose.model("TelemetryData", TelemetryDataSchema);

module.exports = TelemetryData;
