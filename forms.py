from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,TimeField,DateField,IntegerField,RadioField,StringField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError



class EmanetlerSorguForm(FlaskForm):
    Radio = RadioField(' ', choices=[( 'Universal əmanət'),
                                                ( 'Uşaq yığım əmanəti'),
                                                ("Yığım əmanəti"),
                                                ("Saxlanc seyfləri")],validators = [DataRequired()])
    Name = StringField('Adınız',render_kw={'placeholder':'Add First name'},validators = [DataRequired()])
    Sorname = StringField('Soyadiniz',render_kw={'placeholder':'Add Last name'},validators = [DataRequired()])
    prefix = SelectField(" ",choices=[("050"),("055"),("070"),('077')])
    phone = IntegerField(' ',render_kw={'placeholder':'604 19 05'},validators = [DataRequired()])