from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies,get_movie,search_movie

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

  search_movie = request.args.get('movie_query')

  if search_movie:
    return redirect(url_for('search',movie_name = search_movie))
  else:
    return render_template('index.html',message = message, title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movie)

  

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  '''
  view movie page function that returns the movie details page and its data
  '''
  movie = get_movie(movie_id)
  title = f"{movie.title}"
  return render_template('movie.html',movie = movie, title = title )

@app.route('/search/<movie_name>')
def search(movie_name):
  '''
  View Function to display the search results
  '''
  movie_name_list = movie_name.split(" ")
  movie_name_format = "+".join(movie_name_list)
  searched_movies = search_movie(movie_name_format)
  title = f'search results for {movie_name}'
  return render_template('search.html',movies = searched_movies,title = title)