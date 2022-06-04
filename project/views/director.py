from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services.director import DirectorService
from project.setup_db import db

director_ns = Namespace("director")


@director_ns.route("/")
class DirectorView(Resource):
    @director_ns.response(200, "OK")
    def get(self):
        """Get all director"""
        return DirectorService(db.session).get_all()


@director_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @director_ns.response(200, "OK")
    @director_ns.response(404, "Genre not found")
    def get(self, director_id: int):
        try:
            return DirectorService(db.session).get_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Genre not found")
