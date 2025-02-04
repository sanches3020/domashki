import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    conn = sqlite3.connect('Задание 1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, manufacturer, form, price FROM medicines")
    medicines = cursor.fetchall()
    conn.close()
    return render_template("index.html", medicines=medicines) 

if __name__ == '__main__':
    app.run(debug=True)
    