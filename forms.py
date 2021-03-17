import wtforms
from models import Book, Author, Genre


class BookForm(wtforms.Form):
    name = wtforms.StringField(validators=[wtforms.validators.InputRequired(message="You didn't entered any data")], description="Title of the book")
    author = wtforms.SelectField(choices=[(_.id, _.name) for _ in Author.select()], description="Author of the book:")
    genre = wtforms.SelectField(choices=[(_.id, _.name) for _ in Genre.select()], description="Genre of the book:")
    year = wtforms.StringField(validators=[wtforms.validators.InputRequired(message="You didn't entered any data"), wtforms.validators.Regexp("\d{4}", message="Wrong year format")], description="Year of publishing:")

    def save(self):
        Book.create(name=self.name.data,
        author=self.author.data,
        genre=self.genre.data,
        year=self.year.data)


class AuthorForm(wtforms.Form):
    name = wtforms.StringField(validators=[wtforms.validators.InputRequired(message="You didn't entered any data")], description="Enter a new author's name:")

    def save(self):
        Author.create(name=self.name.data)


class GenreForm(wtforms.Form):
    name = wtforms.StringField(validators=[wtforms.validators.InputRequired(message="You didn't entered any data")], description="Enter a new genre name:")

    def save(self):
        Genre.create(name=self.name.data)

