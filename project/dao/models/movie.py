from project.dao.models.base import BaseMixin
from project.setup_db import db


class Movie(BaseMixin, db.Model):
    __tablename__ = "movies"

    title = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    trailer = db.Column(db.Text(), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)

    genre = db.relationship("Genre")
    director = db.relationship("Director")
