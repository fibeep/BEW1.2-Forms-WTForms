from grocery_app.models import GroceryItem, GroceryStore, ItemCategory, User
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import FloatField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from wtforms.widgets.core import Select

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # : Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField("Title", validators=[ DataRequired(), Length(min=3, max=80)])
    address = StringField("Address", validators=[ DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit!')
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # : Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button

    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField("Price")
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField("Photo Url", validators=[URL()])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')


# forms.py

class SignUpForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
