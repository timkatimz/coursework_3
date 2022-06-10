from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("/register/")
class AuthRegisterView(Resource):
    def post(self):
        data = request.json
        return auth_service.create(data), 201


@auth_ns.route("/login/")
class AuthLoginView(Resource):
    def post(self):
        data = request.json
        return auth_service.check_login_data(data), 201

    def put(self):
        data = request.json
        return auth_service.check_token(data), 201


