from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

  title = StringField('Review title',validators=[Required()])
  review = TextAreaField('Movie Review')
  submit = SubmitField('Submit')

class UpdateProfileForm(FlaskForm):
  bio = TextAreaField('Tell us about yourself',validators=[Required()])
  submit = SubmitField('Submit')
