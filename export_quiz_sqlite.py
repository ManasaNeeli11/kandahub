import sqlite3
import json

# Path to old SQLite DB
conn = sqlite3.connect(r"C:\Kandahub\kandahub\db.sqlite3")
cursor = conn.cursor()

# Fetch all quizzes
cursor.execute("SELECT * FROM subhub_quiz;")
rows = cursor.fetchall()

# Get column names
cursor.execute("PRAGMA table_info(subhub_quiz);")
columns = [col[1] for col in cursor.fetchall()]

data = []
for row in rows:
    obj = {
        "model": "subhub.quiz",  # your app name and model name
        "pk": row[0],            # assuming first column is the primary key
        "fields": {columns[i]: row[i] for i in range(1, len(columns))}
    }
    data.append(obj)

# Save to JSON fixture
with open("quiz_fixture.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"{len(rows)} quizzes exported successfully in fixture format.")

conn.close()
