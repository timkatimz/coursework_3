from flask_restx import Namespace, abort, Resource

from project.exceptions import ItemNotFound
from project.services.movie import MovieService
from project.setup_db import db

movie_ns = Namespace("movies")


movie_ns.route("/")
class MoviesView(Resource):
    @movie_ns.response(200, "OK")
    def get(self):
        return MovieService(db.session).get_all()

movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    @movie_ns.response(200, "OK")
    @movie_ns.response(404, "Movie not found")
    def get(self, movie_id: int):
        try:
            return MovieService(db.session).get_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
