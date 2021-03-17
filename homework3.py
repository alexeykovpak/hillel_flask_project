import sqlite3
from flask import Flask, render_template, request, redirect
from models import BookModel, AuthorModel, GenreModel


app = Flask(__name__)


def execute_query(query):
# Establishes connection to the SQLite database file

    with sqlite3.connect('db.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


def get_by_id(table, record_id):
# Returns the name field from Genre or Author tables for specified id

    return execute_query(
        'SELECT * FROM {} WHERE id={}'.format(table, record_id)
    )[0]


@app.route('/')
def all_books():
# Returns the list of all books in the library

    books = execute_query('SELECT * FROM Book')
    return render_template('index.html', books=books, get_by_id=get_by_id)


@app.route('/genre/<int:genre_pk>/')
def books_by_genre(genre_pk):
# Returns the list of all the books with the defined genre

    books = execute_query(f'SELECT * FROM Book WHERE genre="{genre_pk}"')
    return render_template('index.html', books=books, get_by_id=get_by_id)


@app.route('/year/<int:year_pk>/')
def books_by_year(year_pk):
# Returns the list of the books that were published in the defined year

    books = execute_query('SELECT * FROM Book WHERE year={}'.format(year_pk))
    return render_template('index.html', books=books, get_by_id=get_by_id)


@app.route('/create/author/', methods=['GET', 'POST'])
def create_author():
# Adds a new author into the database of the library

    if request.method == 'POST':
        execute_query(f'''INSERT INTO Author (name)
        VALUES ("{request.form['name']}")''')
        return redirect('/')
    return render_template('create_author.html')


@app.route('/create/genre/', methods=['GET', 'POST'])
def create_genre():
# Adds a new genre into the database of the library

    if request.method == 'POST':
        execute_query(
            f'''INSERT INTO Genre (name) VALUES ("{request.form['name']}")'''
        )
        return redirect('/')
    return render_template('create_genre.html')


@app.route('/create/book/', methods=['GET', 'POST'])
def create_book():
# Adds a new book record into the database of the library

    if request.method == 'POST':
        genre_id = execute_query(f'''SELECT id FROM Genre WHERE name="{request.form['genre']}"''')
        if not genre_id:
            execute_query(f'''INSERT INTO Genre (name) VALUES ("{request.form['genre']}")''')
            genre_id = execute_query(f'''SELECT id FROM Genre WHERE name="{request.form['genre']}"''')
        author_id = execute_query(f'''SELECT id FROM Author WHERE name="{request.form['author']}"''')
        if not author_id:
            execute_query(f'''INSERT INTO Author (name) VALUES ("{request.form['author']}")''')
            author_id = execute_query(f'''SELECT id FROM Author WHERE name="{request.form['author']}"''')
        execute_query(
            f'''INSERT INTO Book (name, author, genre, year)
            VALUES ("{request.form['name']}", "{author_id[0][0]}", "{genre_id[0][0]}",
            "{request.form['year']}")'''
        )
        return redirect('/')
    return render_template('create_book.html')


@app.route('/update/book/<int:book_id>/', methods=['GET', 'POST'])
def update_book(book_id):
# Updates values for the book with defined id

    if request.method == 'POST':
        genre_id = execute_query(f'''SELECT id FROM Genre WHERE name="{request.form['genre']}"''')
        if not genre_id:
            execute_query(f'''INSERT INTO Genre (name) VALUES ("{request.form['genre']}")''')
            genre_id = execute_query(f'''SELECT id FROM Genre WHERE name="{request.form['genre']}"''')
        author_id = execute_query(f'''SELECT id FROM Author WHERE name="{request.form['author']}"''')
        if not author_id:
            execute_query(f'''INSERT INTO Author (name) VALUES ("{request.form['author']}")''')
            author_id = execute_query(f'''SELECT id FROM Author WHERE name="{request.form['author']}"''')
        execute_query(f'''UPDATE Book SET name="{request.form['name']}", author="{author_id[0][0]}",
        genre="{genre_id[0][0]}", year="{request.form['year']}" WHERE id={book_id};''')
        return redirect('/')
    book = execute_query(f'SELECT * FROM Book WHERE Book.id={book_id}')
    return render_template('change_book.html', book=book[0], get_by_id=get_by_id)


if __name__ == '__main__':
    app.run(host='127.0.0.1',
        port=5000,
        debug=True,
    )

