# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from config import app
from models import Movie, Director, Genre
from schemas import MovieSchema, GenreSchema, DirectorSchema

api = Api(app)
movie_ns = api.namespace('movies')
director_ns = api.namespace('director')
genre_ns = api.namespace('genre')

@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        query = Movie.query
        if director_id:
            query = query.filter(Movie.director_id == director_id)
        if genre_id:
            query = query.filter(Movie.genre_id == genre_id)
        return MovieSchema(many=True).dump(Movie.query.all()), 200

@movie_ns.route('/<int:id>')
class MovieViews(Resource):
    def get(self, id):
        return MovieSchema().dump(Movie.query.get(id)), 200

if __name__ == '__main__':
    app.run(debug=True)
