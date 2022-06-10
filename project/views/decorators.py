import jwt
from flask import request, abort

from constants import SECRET_KEY, ALGORITHM


def auth(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401, "No authorization")

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except Exception as e:
            abort(401, f"Decode Error {e}")
        return func(*args, **kwargs)
    return wrapper
