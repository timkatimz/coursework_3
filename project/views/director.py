from flask_restx import abort, Namespace, Resource

from project.container import director_service
from project.exceptions import ItemNotFound
directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    def get(self):
        """Get all director"""
        return director_service.get_all()


@directors_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Genre not found")
    def get(self, director_id: int):
        try:
            return director_service.get_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")
