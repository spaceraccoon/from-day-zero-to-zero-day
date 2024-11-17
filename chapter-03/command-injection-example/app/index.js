const express = require("express");
const { ping } = require("./utils.js");

const app = express();

app.get("/ping", (req, res) => {
  const ip = req.query.ip;
  res.send(`Result: \n${ping(ip)}`);
})

app.listen(3000);