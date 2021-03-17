from peewee import DoesNotExist, IntegrityError
from flask import Flask, render_template, request, redirect, abort, flash
from models import Book, Author, Genre
from forms import BookForm, AuthorForm, GenreForm


app = Flask(__name__)
app.secret_key = b'_7#r2M"d6dZf\n\xec]/'


@app.route('/')
def all_books():

    books = Book.select().join_from(Book, Author).join_from(Book, Genre)
    return render_template('index.html', books=books)


@app.route('/genre/<int:genre_pk>/')
def books_by_genre(genre_pk):

    try:
        books = Book.select().join_from(Book, Genre).where(Genre.id == genre_pk)
    except DoesNotExist:
        return abort(404)
    return render_template('index.html', books=books)


@app.route('/year/<int:year_pk>/')
def books_by_year(year_pk):

    try:
        books = Book.select().where(Book.year == str(year_pk))
    except DoesNotExist:
        return abort(404)
    return render_template('index.html', books=books)


@app.route('/create/author/', methods=['GET', 'POST'])
def create_author():

    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(formdata=request.form)
        if form.validate():
            try:
                form.save()
            except IntegrityError:
                flash('The author already exists')
                return redirect('/create/author/')
            flash('The author was successefully added')
            return redirect('/')
    return render_template('create_author.html', form=form)


@app.route('/create/genre/', methods=['GET', 'POST'])
def create_genre():

    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(formdata=request.form)
        if form.validate():
            try:
                form.save()
            except IntegrityError:
                flash('The genre already exists')
                return redirect('/create/genre/')
            flash('The genre was successefully added')
            return redirect('/')
    return render_template('create_genre.html', form=form)


@app.route('/update/book/<int:book_id>/', methods=['GET', 'POST'])
def update_book(book_id):

    form = BookForm()
    book = Book.get(Book.id == book_id)
    if request.method == 'POST':
        form = BookForm(formdata=request.form)
        if form.validate():
            book = Book.get(Book.id == book_id)
            book.name = form.name.data
            book.author = form.author.data
            book.genre = form.genre.data
            book.year = form.year.data
            book.save()
            flash('The book was successfully updated')
            return redirect('/') 
    try:
        updating_book = Book.get(Book.id == book_id)
    except DoesNotExist:
        return abort(404)
    return render_template('change_book.html', form=form, book=book)


@app.route('/create/book/', methods=['GET', 'POST'])
def create_book():

    form = BookForm()
    if request.method == 'POST':
        form = BookForm(formdata=request.form)
        if form.validate():
            form.save()
            flash('The book was successfully added')
            return redirect('/')
    return render_template('create_book.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1',
        port=5000,
        debug=True,
    )

