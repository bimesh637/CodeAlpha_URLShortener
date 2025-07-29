from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random
import os

app = Flask(__name__)

# ─────────────────────────────────────────────────────
#  Initialize SQLite DB
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  short TEXT UNIQUE,
                  original TEXT)''')
    conn.commit()
    conn.close()

init_db()

# ─────────────────────────────────────────────────────
#  Generate short code
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ─────────────────────────────────────────────────────
#  Home page (Optional frontend)
@app.route('/')
def home():
    return render_template('index.html')

# ─────────────────────────────────────────────────────
#  API: Shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.form if request.form else request.json
    original_url = data.get('url')

    if not original_url:
        return {"error": "No URL provided"}, 400

    short_code = generate_short_code()
    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO urls (short, original) VALUES (?, ?)", (short_code, original_url))
    conn.commit()
    conn.close()

    return {"short_url": f"http://localhost:5000/{short_code}"}

# ─────────────────────────────────────────────────────
#  Redirect to original URL
@app.route('/<short_code>')
def redirect_url(short_code):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT original FROM urls WHERE short = ?", (short_code,))
    result = c.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "URL Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
