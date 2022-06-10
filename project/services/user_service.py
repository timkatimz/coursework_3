import jwt
from flask_restx import abort

from constants import SECRET_KEY, ALGORITHM
from project.tools.security import generate_password_digest


class UserService:

    def __init__(self, dao):
        self.dao = dao

    def get_profile(self, jwt_token):
        return self.get_user_by_email(jwt_token)

    def update_profile(self, jwt_token, user_data):
        user = self.get_user_by_email(jwt_token)

        user.name = user_data.get("name", None)
        user.surname = user_data.get("surname", None)
        user.favourite_genre = user_data.get("favourite_genre", None)

        return self.dao.update_user_profile(user)

    def update_password(self, jwt_token, passwords):
        user = self.get_user_by_email(jwt_token)

        old_password = generate_password_digest(passwords["old_password"])
        if user.password != old_password:
            abort(401, "Incorrect password")
        new_password = generate_password_digest(passwords["new_password"])

        user.password = new_password

        return self.dao.update_user_password(user)

    def get_user_by_email(self, jwt_token):
        token = jwt_token.split("Bearer ")[-1]
        user = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = user.get("email")
        user = self.dao.get_user_profile(email)
        return user
