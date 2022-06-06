from flask import current_app
from sqlalchemy import desc
from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, pk):
        return self.session.query(Movie).filter(Movie.id == pk).one_or_none()

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_pagination(self, page):
        return self.session.query(Movie).limit(
            current_app.config["ITEMS_PER_PAGE"]).offset(
            (page - 1) * current_app.config["ITEMS_PER_PAGE"]).all()

    def get_new(self):
        return self.session.query(Movie).order_by(desc(Movie.year)).all()
