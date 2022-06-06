from marshmallow import fields, Schema

from project.schemas.director_schema import director_schema
from project.schemas.genre_schema import genre_schema


class MovieSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Int(required=True)
    rating = fields.Float(required=True)
    genre = fields.Nested(genre_schema)
    director = fields.Nested(director_schema)


movie_schema = MovieSchema()
