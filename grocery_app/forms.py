from grocery_app.models import GroceryItem, GroceryStore, ItemCategory
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import FloatField
from wtforms.validators import DataRequired, Length, URL
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

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button

    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField()
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField("Photo Url", validators=[URL()])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')

