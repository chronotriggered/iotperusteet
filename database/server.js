const express = require("express");
const sqlite3 = require("sqlite3");
const app = express();
const port = 3000;

app.use(express.json());

const db = new sqlite3.Database("./ElmonDatabase.db", (err) => {
  if (err) return console.error(err.message);
  console.log("Connected to the database.");
});

db.run(`CREATE TABLE IF NOT EXISTS data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  temperature TEXT NOT NULL,
  humidity TEXT NOT NULL,
  time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)`);

app.get("/api/sensor", (req, res) => {
  res.json({
    temperature: 22.5,
    humidity: 55,
    status: "OK",
  });
});

app.get("/api/data", (req, res) => {
  log("In get endpoint");
  db.all("SELECT * FROM users", [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

app.post("/api/data", (req, res) => {
  log("In post endpoint");
  const { temperature, humidity, time } = req.body;
  db.run(
    `INSERT INTO data (temperature, humidity, time) VALUES (?, ?, ?)`,
    [temperature, humidity, time],
    function (err) {
      if (err) return res.status(400).json({ error: err.message });
      res.status(201).json({ id: this.lastID, temperature, humidity, time });
    }
  );
});

app.listen(port, () => {
  console.log(`Server running at
http://localhost:${port}`);
});
