import sqlite3
from flask import Flask, render_template, request,redirect, url_for, flash


app = Flask(__name__)
app.secret_key = '1234'

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/upload/', methods=['POST']) 
def save_post():
    title = request.form['title']
    description = request.form['description']  
    image = request.files.get('image')
    file_name = image.filename

    print(image.filename)
    print(image.name)
    print(image.content_type)  
    image.save(f'static/uploads/{file_name}')

    conn = sqlite3.connect('database_name.db') 
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bd1 (title,file_name,description)
        VALUES (?, ?, ?)
    """, (title,file_name,description))
    conn.commit()
    conn.close()

    flash('Пост успешно сохранен!', 'success')
    return redirect (url_for("add"))

@app.route('/all_post/') 
def all_post():
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bd1")
    posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)






    

