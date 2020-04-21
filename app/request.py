from app import app
import urllib.request, json
from .models import movie

Movie = movie.Movie
#getting the api key
api_key = app.config['MOVIE_API_KEY']

#Getting the movie Base URL
base_url = app.config['MOVIE_API_BASE_URL']

def process_results(movie_list):
  '''
  transforms the movie result into a list of objects

  args:
  movie_list : a list of dictionaries that contains movie details

  returns:
  movie_results : A list of movie objects
  '''
  movie_results = []
  for movie_item in movie_list:
    id = movie_item.get('')
    title = movie_item.get('original_title')
    overview = movie_item.get('overview')
    poster = movie_item.get('poster_path')
    vote_average = movie_item.get('vote_average')
    vote_count = movie_item.get('vote_count')

    if poster:
      movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
      movie_results.append(movie_object)

  return movie_results
  
def get_movies(category):
  '''
  function that gets the json response from the request ur;
  '''
  get_movies_url = base_url.format(category,api_key)

  with urllib.request.urlopen(get_movies_url) as url:
    get_movies_data = url.read()
    get_movies_response = json.loads(get_movies_data)

    movie_results = None

    if get_movies_response['results']:
      movie_results_list = get_movies_response['results']
      movie_results = process_results(movie_results_list)

  return movie_results