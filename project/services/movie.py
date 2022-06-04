from project.dao.movie import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import movie_schema
from project.services.base import BaseService


class MovieService(BaseService):

    def get_by_id(self, pk):
        movie = MovieDAO(self._db_session).get_by_id(pk)
        if not movie:
            raise ItemNotFound
        return movie_schema.dump(movie)

    def get_all(self):
        movies = MovieDAO(self._db_session).get_all()
        return movie_schema.dump(movies, many=True)