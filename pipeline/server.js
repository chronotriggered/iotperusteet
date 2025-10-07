import path from "path";
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

import fetch from "node-fetch";
import express, { json } from "express";
import sqlite3 from "sqlite3";
const app = express();

app.use(json());
app.use(express.static(path.join(__dirname, "public")));

const API_KEY = "B5Z7032Q1KD9MNK6";
const BASE_URL = "https://api.thingspeak.com/channels/3083804/feeds.json?";
const PORT = 3000;
const WEBHOOK =
  "https://discord.com/api/webhooks/1422173095879507969/vQQ_ksXiJe_mSFKglShgpuzaATHC7zKMErb2a8P5h2xIr5-OQ9oLkvYLgMrcHVGzDGtH";

const db = new sqlite3.Database("./ElmonDatabase.db", (err) => {
  if (err) return console.error(err.message);
  console.log("Connected to SQLite database");
});

db.run(`CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature INTEGER NOT NULL,
    humidity INTEGER NOT NULL,
    time DATETIME DEFAULT CURRENT_TIMESTAMP
    )`);

const fetchDataAndStore = async () => {
  const response = await fetch(`${BASE_URL}api_key=${API_KEY}&results=2`).then(
    (res) => res.json()
  );

  const time = response.feeds[1].created_at;
  const temperature = response.feeds[1].field1;
  const humidity = response.feeds[1].field2;

  db.run(
    "INSERT INTO data (temperature, humidity, time) VALUES (?, ?, ?)",
    [temperature, humidity, time],
    function (err) {
      if (err) return console.error(err.message);
      console.log(`A row has been inserted with rowid ${this.lastID}`);
    }
  );
  if (temperature > 30 || humidity > 70) {
    const msg = {
      content: `🚨 ALERT!\n🌡️ Temp: ${temperature}°C\n💧 Humidity: ${humidity}%`,
    };

    await fetch(WEBHOOK, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(msg),
    });
  }
};

setInterval(() => {
  fetchDataAndStore();
}, 15000);

app.get("/data", (req, res) => {
  db.all("SELECT * FROM data", [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ data: rows });
  });
});

app.post("/discord", async (req, res) => {
  const { temp, hum } = req.body;

  const message = {
    content: `🌡 Temp: ${temp}°C\n💧 Humidity: ${hum}%`,
  };

  await fetch(discord_webhook_url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(message),
  });

  res.send("Sent to Discord");
});

app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
