import sqlite3
import os

db_path = os.path.join("database", "resume_data.db")

if not os.path.exists(db_path):
    print("❌ Database file not found!")
    exit()

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT * FROM results")
rows = cur.fetchall()

if not rows:
    print("⚠️ No data stored yet.")
else:
    print("\nID | Resume Name | Match % | Matched Skills | Missing Skills | Date")
    print("-" * 90)
    for row in rows:
        print(row)

conn.close()
