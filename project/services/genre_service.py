from project.exceptions import ItemNotFound
from project.schemas.genre_schema import genre_schema


class GenreService:

    def __init__(self, dao):
        self.dao = dao

    def get_item_by_id(self, pk):
        genre = self.dao.get_by_id(pk)
        if not genre:
            raise ItemNotFound
        return genre_schema.dump(genre)

    def get_all_genres(self):
        genres = self.dao.get_all()
        return genre_schema.dump(genres, many=True)
