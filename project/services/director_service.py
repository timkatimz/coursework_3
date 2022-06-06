
from project.exceptions import ItemNotFound
from project.schemas.director_schema import director_schema


class DirectorService:

    def __init__(self, dao):
        self.dao = dao

    def get_by_id(self, pk):
        director = self.dao.get_by_id(pk)
        if not director:
            raise ItemNotFound
        return director_schema.dump(director)

    def get_all(self):
        directors = self.dao.get_all()
        return director_schema.dump(directors, many=True)
