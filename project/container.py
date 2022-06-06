from project.dao.genre_dao import GenreDAO
from project.dao.director_dao import DirectorDAO
from project.dao.movie_dao import MovieDAO
from project.dao.user_dao import UserDAO
from project.services.director_service import DirectorService
from project.services.genre_service import GenreService
from project.services.movie_service import MovieService
from project.services.user_service import UserService
from project.setup_db import db

user_dao = UserDAO(db.session)
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
movie_dao = MovieDAO(db.session)

user_service = UserService(user_dao)
director_service = DirectorService(director_dao)
genre_service = GenreService(genre_dao)
movie_service = MovieService(movie_dao)
