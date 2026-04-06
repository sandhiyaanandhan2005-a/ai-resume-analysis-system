from flask import Flask, request, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

DB_PATH = os.path.join("database", "resume_data.db")

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS resume_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_name TEXT,
            match_percent REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/save", methods=["POST"])
def save_result():
    data = request.json
    resume_name = data["resume_name"]
    match_percent = data["match_percent"]

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO resume_results (resume_name, match_percent, date) VALUES (?, ?, ?)",
        (resume_name, match_percent, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
