import calendar
import datetime

import jwt
from flask_restx import abort

from constants import SECRET_KEY, TOKEN_EXPIRE_MINUTES, ALGORITHM, TOKEN_EXPIRE_DAYS
from project.tools.security import generate_password_digest


class UserService:

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

        try:
            min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
            data["exp"] = calendar.timegm(min15.timetuple())
            access_token = jwt.encode(data,
                                      key=SECRET_KEY, algorithm=ALGORITHM)
            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
            data["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data,
                                       key=SECRET_KEY, algorithm=ALGORITHM)
            tokens = {"access_token": access_token, "refresh_token": refresh_token}
        except jwt.PyJWTError as e:
            return f"{e}"
        return tokens

    def check_tokens(self, data):
        refresh_token = data["refresh_token"]
        if not refresh_token:
            abort(400)
        try:
            jwt.decode(jwt=refresh_token, key=SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.DecodeError as e:
            return f"{e}"

        try:
            min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
            data["exp"] = calendar.timegm(min15.timetuple())
            access_token = jwt.encode(data,
                                      key=SECRET_KEY, algorithm=ALGORITHM)

            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
            data["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data,
                                       key=SECRET_KEY, algorithm=ALGORITHM)
            tokens = {"access_token": access_token, "refresh_token": refresh_token}
        except jwt.PyJWTError as e:
            return f"{e}"
        return tokens


