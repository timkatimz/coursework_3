from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api

from project.setup_db import db
from project.views.auth import auth_ns
from project.views.director import directors_ns
from project.views.movies import movies_ns
from project.views.genres import genres_ns
from project.views.user import user_ns

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 4",
    doc="/docs",
)

cors = CORS()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template("index.html")

    db.init_app(app)
    api.init_app(app)

    # Register end-points
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)

    return app
