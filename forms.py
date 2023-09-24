from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import URL


class AddCupcakeForm(FlaskForm):
    """Form to add a new cupcake"""
    flavor = StringField("Flavor")
    size = StringField("Size")
    rating = FloatField("Rating")
    image = StringField(validators=[URL()])
