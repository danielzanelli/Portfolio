const express = require("express");
const session = require("express-session");
const MongoDBStore = require("connect-mongodb-session")(session);
const mongoose = require("mongoose");
const router = express.Router();
const cors = require("cors");

const app = express();

app.use(cors({ origin: true, credentials: true }));
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Methods", "POST, GET, OPTIONS");
  next();
});

//const HOST = "localhost";
const HOST = "0.0.0.0";
const PORT = 5000;
const SESS_SECRET = "secret";
const IS_PROD = false;
const COOKIE_NAME = "session-id";

const MongoURI = "mongodb://localhost:27017/dashboard";
const MAX_AGE = 1000 * 60 * 60 * 2; // 2hr

mongoose
  .connect(MongoURI, {
    useNewUrlParser: true,
  })
  .then(() => console.log("MongoDB connected..."))
  .catch((err) => console.log(err));

const mongoDBstore = new MongoDBStore({
  uri: MongoURI,
  collection: "mySessions",
});

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(
  session({
    name: COOKIE_NAME,
    secret: SESS_SECRET,
    resave: true,
    saveUninitialized: false,
    store: mongoDBstore,
    cookie: {
      maxAge: MAX_AGE,
      sameSite: false,
      secure: IS_PROD,
    },
  })
);

app.listen(PORT, HOST, () =>
  console.log(`Server started on http://${HOST}:${PORT}`)
);

app.use("/api/users", require("./routes/users"));
