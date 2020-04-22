from flask import render_template
from app import app
from .request import get_movies

#views

@app.route('/')
def index():
  '''
  view root page function that returns the index page and its data
  '''
  message = "Hello World"

  #getting popular movie
  popular_movies = get_movies('popular')
  upcoming_movies = get_movies('upcoming')
  now_showing_movie = get_movies('now_playing')


  title = 'Home - Welcome to the Best Movie Review Website online '
  return render_template('index.html',message = message, title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movie)

  

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  '''
  view movie page function that returns the movie details page and its data
  '''
  movie_title = f"The movie {movie_id}"
  return render_template('movie.html',id = movie_id, title = movie_title )