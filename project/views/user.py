from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service

auth_ns = Namespace("auth")


@auth_ns.route("/register/")
class UserRegisterView(Resource):
    def post(self):
        data = request.json
        return user_service.create(data), 201

@auth_ns.route("/login/")
class UserLoginView(Resource):
    def post(self):
        data = request.json
        return user_service.check_login_data(data), 201

    def put(self):
        data = request.json
        return user_service.check_tokens(data), 201


