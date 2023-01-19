import random

from flask import render_template

from app import app
from app.models import User, Movie


@app.route('/')
@app.route('/index')
def index():
    username = 'Bogdan'
    user = User.query.filter_by(username=username).first()
    movies_from_db = Movie.query.filter_by(user_id=user.id).all()
    movies = [movie.title for movie in movies_from_db]

    movie_index = random.randint(0, len(movies) - 1)
    user = {'username': user.username, 'movie': movies[movie_index], 'movies': movies}
    return render_template('index.html', title='Home Page', user=user)


@app.route('/name')
def hello_name():
    return 'Hello, Python Group!'


@app.route('/name/<given_name>')
def hello_given_name(given_name):
    return f'Hello, {given_name}'
