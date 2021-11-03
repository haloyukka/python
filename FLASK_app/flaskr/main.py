from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

# トップ画面にアクセスした時に実行される
@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close()

    books = []
    for row in db_books:
        books.append({'title': row[0], 'price': row[1], 'arrival_day': row[2]})

    # books =[
    #     # {'title': 'はらぺこあおむし',
    #     # 'price': 1200,
    #     # 'arrival_day': '2020年7月12日'},
    #     # {'title': 'ぐりとぐら',
    #     # 'price': 990,
    #     # 'arrival_day': '2020年7月13日'},
    # ]

    return render_template(
        'index.html',
        books=books
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?, ?, ?)',
                [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index'))
