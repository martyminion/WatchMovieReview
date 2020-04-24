import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the movie class
  '''

  def setUp(self):
    '''
    set up method that will run for every test
    '''
    self.new_movie = Movie(1234,"Python Must Be Crazy","A Thrilling New Python Series","https://image.tmdb.org/t/p/w500/khsjha27hbs",8.5,129993)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_movie,Movie))
  
  def test_init(self):
    '''
    tests if the movie class is initialized correctly
    '''
    self.assertEqual(self.new_movie.id,1234)
    self.assertEqual(self.new_movie.title,"Python Must Be Crazy" )
    self.assertEqual(self.new_movie.overview,"A Thrilling New Python Series")
    self.assertEqual(self.new_movie.poster,"https://image.tmdb.org/t/p/w500/khsjha27hbs"+"https://image.tmdb.org/t/p/w500/khsjha27hbs")
    self.assertEqual(self.new_movie.vote_average,8.5)
    self.assertEqual(self.new_movie.vote_count,129993)
