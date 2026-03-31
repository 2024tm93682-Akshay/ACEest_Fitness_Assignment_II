from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "aceest_fitness.db"

def get_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        program TEXT,
        membership_status TEXT
    )
    """)

    conn.commit()
    conn.close()

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return "ACEest Fitness Backend Running 🚀"

@app.route('/clients', methods=['GET'])
def get_clients():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/add_client', methods=['POST'])
def add_client():
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute("INSERT OR IGNORE INTO clients (name, membership_status) VALUES (?,?)",
                (data['name'], "Active"))

    conn.commit()
    conn.close()
    return jsonify({"status": "client added"})

@app.route('/delete_client/<name>', methods=['DELETE'])
def delete_client(name):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM clients WHERE name=?", (name,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

# ---------------- MAIN ----------------

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)