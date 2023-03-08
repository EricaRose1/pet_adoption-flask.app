from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, URLField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length


class AddPetForm(FlaskForm):
    '''form to add new pats'''
    name = StringField('Pet Name', 
                        validators=[InputRequired()],)
    species = StringField('Species')
                            # choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],)
    photo_url = URLField('Photo URL', 
                            validators = [Optional(), URL()],)
    age = IntegerField('Age', 
                        validators = [Optional(), NumberRange(min=0, max=30, message=None) ],)
    notes = StringField('Notes', 
                        validators=[Optional(), Length(min=10)],)

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],)

    notes = TextAreaField(
        "Notes",
        validators=[Optional(), Length(min=10)],)

    available = BooleanField("Available?")