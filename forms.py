from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,TimeField,DateField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

# def validate_yourPoint(form, field):
#     if (len(str(field.data)) > 7):
#         raise ValidationError('Nomre maksimum 7 eded ola biler')
    
class SorguForm(FlaskForm):
    Branch = SelectField('Select a branch', choices=[('Admin'), ('Regular')])
    Service = SelectField('Select service type', choices=[('Admin'), ('Regular')])
    Date = DateField('Select date', validators=[DataRequired()], render_kw={"min": "2024-06-01", "max": "2024-07-30"})
    Time = SelectField("Select time",choices=[("10:00:00"),("12:00:00")])
    prefix = SelectField(" ",choices=[("050"),("055"),("070"),('077')])
    phone = IntegerField(' ',render_kw={'placeholder':'604 19 05'},validators = [DataRequired()])


    