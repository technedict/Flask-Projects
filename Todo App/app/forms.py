from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    todotext = StringField('Add an Item', validators=[DataRequired()])
    submit = SubmitField('Add')