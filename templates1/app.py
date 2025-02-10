import sqlite3
from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/save_post/') 
def save_post():
    title = request.form['title']
    file_name = request.form['file_name']
    description = request.form['description']
    
    image = request.files.get('image')
    print(image.filename)
    print(image.name)
    print(image.content_type)
    image.save(f'D:\college\flask\static\uploads')

    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bd1 (title,file_name,description)
        VALUES (?, ?, ?)
    """, (title,file_name,description))
    conn.commit()
    conn.close()

    return redirect (url_for("add.html"))

@app.route('/all_post/') 
def all_post():
    if request.method== 'POST':
        title = request.form['title']
        file_name = request.form['file_name']
        description = request.form['description']

    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()
    cursor.execute("""
                        SELECT * FROM bd1 WHERE title= ? AND file_name=? AND description=?""",[title,file_name,description])
    if cursor.fetchone():
       conn.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)






    

