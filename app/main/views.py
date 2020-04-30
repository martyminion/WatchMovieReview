from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_movies,get_movie,search_movie
from ..models import Review,User
from .forms import ReviewForm,UpdateProfileForm
from .. import db
from flask_login import login_required #checks if user is authenticated, else redirects to login page


#views

@main.route('/')
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
    return redirect(url_for('.search',movie_name = search_movie))
  else:
    return render_template('index.html',message = message, title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movie)

  

@main.route('/movie/<int:movie_id>')
def movie(movie_id):
  '''
  view movie page function that returns the movie details page and its data
  '''
  movie = get_movie(movie_id)
  title = f"{movie.title}"
  reviews = Review.get_reviews(movie.id)
  return render_template('movie.html',movie = movie, title = title, reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
  '''
  View Function to display the search results
  '''
  movie_name_list = movie_name.split(" ")
  movie_name_format = "+".join(movie_name_list)
  searched_movies = search_movie(movie_name_format)
  title = f'search results for {movie_name}'
  return render_template('search.html',movies = searched_movies,title = title)

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
  form = ReviewForm()
  movie = get_movie(id)

  if form.validate_on_submit():
    title = form.title.data
    review = form.review.data
    new_review = Review(movie.id,title,movie.poster,review)
    new_review.save_review()
    return redirect(url_for('.movie',movie_id = movie.id))

  title = f'{movie.title} review'
  return render_template('new_review.html',title = title, review_form = form, movie = movie)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)

  return render_template("profile/profile.html",user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)

  form = UpdateProfileForm()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname = user.username))
  return render_template('profile/update.html',form = form)