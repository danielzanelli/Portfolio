const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");

const User = require("../models/User");

/*
router.post("/register", (req, res) => {
  const { name, email, password } = req.body;

  // Check required fields
  if (!name || !email || !password) {
    return res.status(400).json({ msg: "Please enter all fields" });
  }
  //Check password length
  if (password.length < 6) {
    return res
      .status(400)
      .json({ msg: "Password should be atleast 6 characters long" });
  }

  User.findOne({ email: email }).then((user) => {
    if (user) return res.status(400).json({ msg: "User already exists" });
  });

  //New User created
  const newUser = new User({
    name: name,
    email: email,
    password: password,
  });

  //Password hashing
  bcrypt.genSalt(12, (err, salt) =>
    bcrypt.hash(newUser.password, salt, (err, hash) => {
      if (err) throw err;

      newUser.password = hash;
      // Save user
      newUser
        .save()
        .then(
          res.json({
            msg: "Successfully Registered",
          })
        )
        .catch((err) => console.log(err));
    })
  );
});
*/

router.post("/login", (req, res) => {
  const { email, password } = req.body;
  // basic validation
  if (!email || !password) {
    return res.status(400).json({ msg: "Please enter all fields" });
  }
  //check for existing user
  User.findOne({ email }).then((user) => {
    if (!user) return res.status(400).json({ msg: "User does not exist" });

    // Validate password
    bcrypt.compare(password, user.password).then((isMatch) => {
      if (!isMatch) return res.status(400).json({ msg: "Invalid credentials" });

      const sessUser = {
        id: user.id,
        name: user.name,
        email: user.email,
        origin: req.headers.origin,
      };
      req.session.user = sessUser; // Auto saves session data in mongo store

      user.last_login = Date.now();
      user.save();

      res.json({
        msg: "Logged In Successfully",
        sessUser,
      });
    });
  });
});

router.delete("/logout", (req, res) => {
  req.session.destroy((err) => {
    //delete session data from store, using sessionID in cookie
    req.session = null;
    if (err) throw err;
    res.clearCookie("session-id"); // clears cookie containing expired sessionID
    res.send("Logged out successfully");
  });
});

router.get("/authchecker", (req, res) => {
  const sessUser = req.session.user;
  if (sessUser) {
    return res.json({ msg: "OK" });
  } else {
    return res.status(401).json({ msg: "Unauthorized" });
  }
});

module.exports = router;
