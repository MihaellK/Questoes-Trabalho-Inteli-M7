from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    # post_text = db.Column(db.String(400), nullable=False)

def create_table(app):

    with app.app_context():
        db.create_all()


def main():
    create_table()

if __name__ == "__main__":
    main()