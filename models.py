from peewee import SqliteDatabase, Model, AutoField, CharField, ForeignKeyField

db = SqliteDatabase('db1.db')#, pragmas={'foreign_keys': 1})


class Author(Model):
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=50, unique=True)

    class Meta():
        database = db


class Genre(Model):
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=50, unique=True);

    class Meta():
        database = db


class Book(Model):
    id = AutoField(primary_key=True, unique=True)
    name = CharField(max_length=100)
    author = ForeignKeyField(Author, backref='books')
    genre = ForeignKeyField(Genre, backref='books')
    year = CharField(max_length=4)

    class Meta():
        database = db


if __name__ == '__main__':
    db.create_tables([Author, Genre, Book])

