from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genre import genre_schema
from project.services.base import BaseService


class GenresService(BaseService):
    def get_item_by_id(self, pk):
        genre = GenreDAO(self._db_session).get_by_id(pk)
        if not genre:
            raise ItemNotFound
        return genre_schema.dump(genre)

    def get_all_genres(self):
        genres = GenreDAO(self._db_session).get_all()
        return genre_schema.dump(genres, many=True)
