from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = "users"

    email = db.Column(db.Text(), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    name = db.Column(db.Text())
    surname = db.Column(db.Text())
    favorite_genre = db.Column(db.Text())




#
# - **id** - первичный ключ
# - **email -** по нему будет осуществлен доступ на сайт (*уникальное*)
# - **password** — не забывайте, что пароль тут будет в хешированном виде
# - name - имя
# - surname - фамилия
# - favorite_genre - любимый жанр