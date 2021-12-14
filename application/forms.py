from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms import validators 
from wtforms.validators import DataRequired

class AddBeds(FlaskForm):
    bed_name = StringField('Enter bed name', validators=[DataRequired()])
    bed_length =IntegerField('Enter bed length(cm):', validators=[DataRequired()])
    bed_width =IntegerField('Enter bed width(cm)', validators=[DataRequired()])
    bed_aspect =SelectField('Select aspect:', 
    choices=[('north','North'), ('south', 'South'), ('west', 'West'), ('east', 'East'), ('south-west', 'South-West'), ('south-east', 'South-East'), ('north-east', 'North-East'), ('north-west', 'North-West')],
    validators=[DataRequired()])
    submit = SubmitField('Add Bed')

class AddPlants(FlaskForm):
    plant_name = StringField('Enter a plant name', validators=[DataRequired()])
    plant_bed = SelectField('Select a bed:', choices=[], validators = [DataRequired()])
    submit = SubmitField('Add Plant')