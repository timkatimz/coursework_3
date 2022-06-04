from project.dao.director import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.director import director_schema
from project.services.base import BaseService


class DirectorService(BaseService):

    def get_by_id(self, pk):
        director = DirectorDAO(self._db_session).get_by_id(pk)
        if not director:
            raise ItemNotFound
        return director_schema.dump(director)

    def get_all(self):
        directors = DirectorDAO(self._db_session).get_all()
        return director_schema.dump(directors, many=True)
