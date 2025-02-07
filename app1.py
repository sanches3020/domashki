from email import message
import sqlite3
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key='1234'

@app.route("/register/")
def register_page():
    return render_template('register.html')

@app.route("/save_register/", methods=["POST"])
def save_register():
    name = request.form['name']
    last_name = request.form['last_name']
    patronymic = request.form['patronymic']
    gender = request.form.get("gender")
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bd (last_name, name, patronymic, gender, email, username, password)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (last_name, name, patronymic, gender, email, username, password))
    conn.commit()
    conn.close()

    return render_template("register.html")


@app.route("/authorization/", methods=["POST", "GET"])
def login ():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Введите логин {username} и пароль {password}'
    return render_template("login.html", message=' Вы авторизованы')

@app.route("/authorization/", methods=["POST", "GET"])
def result ():
    if request.method == 'POST':

        login = request.form['username']
        if login == 'username':
            flash('Успешно', 'success')
            render_template('authorization.html')
        else:
         flash('Неверный логин или пароль', 'danger')
         return render_template('login.html')
        render_template('authorization.html')    

if __name__ == '__main__':
    app.run(debug=True)