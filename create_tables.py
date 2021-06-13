from sqlite3 import connect
from flask import Flask


app = Flask('__name__')


def execute_query(query):
# Establishes connection to the SQLite database file

    with sqlite3.connect('db.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


@app.route('/create/tables/')
def create_tables():
# Creating Book, Genre and Author tables without SQLAlchemy application

    execute_query('PRAGMA foreign_keys=on;')
    execute_query('''
        CREATE TABLE Book(
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        author INTEGER NOT NULL,
        genre INTEGER NOT NULL,
        year INTEGER NOT NULL,
        FOREIGN KEY(author) REFERENCES Author(id),
        FOREIGN KEY(genre) REFERENCES Genre(id));
        ''')
    execute_query('''
        CREATE TABLE Author(
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT UNIQUE NOT NULL);
        ''')
    execute_query('''
        CREATE TABLE Genre(
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT UNIQUE NOT NULL);
        ''')


if __name__ == '__main__':
    create_tables()

