import calendar
import datetime

import jwt
from flask_restx import abort

from constants import SECRET_KEY, TOKEN_EXPIRE_MINUTES, ALGORITHM, TOKEN_EXPIRE_DAYS
from project.tools.approve_tokens import approve_tokens
from project.tools.security import generate_password_digest


class AuthService:

    def __init__(self, dao):
        self.dao = dao

    def create(self, data):
        email = data["email"]
        open_password = data["password"]

        password = generate_password_digest(open_password)
        login_data = {"email": email, "password": password}

        return self.dao.create(login_data)

    def check_login_data(self, data):
        email = data["email"]
        open_password = data["password"]
        user = self.dao.get_one(email)
        if not user:
            abort(401)

        password = generate_password_digest(open_password)
        if user.password != password:
            abort(401)

        return approve_tokens(data)

    def check_token(self, data):
        refresh_token = data["refresh_token"]
        if not refresh_token:
            abort(400)
        try:
            user_data = jwt.decode(jwt=refresh_token, key=SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.DecodeError as e:
            return f"{e}"

        return approve_tokens(user_data)




