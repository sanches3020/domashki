import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Задание 1.db')
    return conn

@app.route('/glavnoe/')
def glavnoe_page():
    return render_template('glavnoe.html')

@app.route('/preparaty/')
def preparaty_page():

    name = request.args.get('name', '')
    manufacturer = request.args.get('manufacturer', '')
    form = request.args.get('form', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT name, manufacturer, form, price FROM medicines WHERE name LIKE ? OR manufacturer LIKE ? OR form LIKE ?"
    cursor.execute(query, (f'%{name}%', f'%{manufacturer}%', f'%{form}%'))
    medicines = cursor.fetchall()

    conn.close()

    return render_template('preparaty.html', medicines=medicines)

if __name__ == '__main__':
    app.run(debug=True)