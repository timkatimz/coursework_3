from project.setup_db import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    trailer = db.Column(db.Text(), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)

    genre = db.relationship("Genre")
    director = db.relationship("Director")
