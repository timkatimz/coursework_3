from project.setup_db import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    name = db.Column(db.Text())
    surname = db.Column(db.Text())
    favourite_genre = db.Column(db.Integer)

