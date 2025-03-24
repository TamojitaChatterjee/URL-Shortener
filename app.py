#flask

from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

db_name = "urls.db"

def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        long_url TEXT NOT NULL,
        short_url TEXT UNIQUE NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM urls WHERE short_url = ?", (short_url,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return redirect(result[0])
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
