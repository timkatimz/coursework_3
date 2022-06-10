from flask import request
from flask_restx import Namespace, abort, Resource

from project.container import movie_service
from project.exceptions import ItemNotFound

movies_ns = Namespace("movies")



@movies_ns.route("/")
class MoviesView(Resource):
    @movies_ns.response(200, "OK")
    def get(self):
        page = request.args.get("page", type=int)
        status = request.args.get("status", type=str)
        return movie_service.get_all(page, status)



@movies_ns.route("/<int:mid>/")
class MovieView(Resource):
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie not found")
    def get(self, mid):
        try:
            return movie_service.get_by_id(mid)
        except ItemNotFound:
            abort(404, message="Movie not found")
