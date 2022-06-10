from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import user_service
from project.schemas.user_schema import user_schema
from project.views.decorators import auth

user_ns = Namespace("user")


@user_ns.route("/")
class UserView(Resource):
    @auth
    def get(self):
        if "Authorization" not in request.headers:
            abort(401, "No authorization data")
        data = request.headers["Authorization"]
        user = user_service.get_profile(data)
        return user_schema.dump(user)

    @auth
    def patch(self):
        if "Authorization" not in request.headers:
            abort(401, "No authorization data")
        jwt_token = request.headers["Authorization"]
        try:
            user_data = request.json
        except Exception as e:
            return f"Profile update data has not been transferred: {e}"
        return user_service.update_profile(jwt_token, user_data)


@user_ns.route("/password/")
class UserPasswordView(Resource):
    @auth
    def put(self):
        if "Authorization" not in request.headers:
            abort(401, "No authorization data")
        jwt_token = request.headers["Authorization"]
        try:
            passwords = request.json
        except Exception as e:
            return f"Password update data has not been transferred: {e}"
        return user_service.update_password(jwt_token, passwords)
