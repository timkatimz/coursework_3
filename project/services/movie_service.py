from project.exceptions import ItemNotFound
from project.schemas.movie_schema import movie_schema


class MovieService:

    def __init__(self, dao):
        self.dao = dao

    def get_by_id(self, pk):
        movie = self.dao.get_by_id(pk)
        if not movie:
            raise ItemNotFound
        return movie_schema.dump(movie)

    def get_all(self, page=None, status=None):
        if page:
            movies = self.dao.get_all_pagination(page)
        elif status:
            movies = self.dao.get_new()
        else:
            movies = self.dao.get_all()
        return movie_schema.dump(movies, many=True)

