from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,TimeField,DateField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

# def validate_yourPoint(form, field):
#     if (len(str(field.data)) > 7):
#         raise ValidationError('Nomre maksimum 7 eded ola biler')
    
class SorguForm(FlaskForm):
    Branch = SelectField('Select a branch', choices=[('Seçin'), ('Nəsimi filialı (Bül-bül pr.30)'),
                                                    ('Nizami filialı (Sarayevo küç. 26c)'), ('Səbail Filialı (A.Məhərrəmov küç. 33A)'),
                                                    ('Nərimanov filialı (İ.Hidayətzadə küç.49/51)'), ('Yasamal filialı (Şərifzadə küç.408)'),
                                                    ('Baş Ofis (Bakı şəh.,Nəsimi ray., 28 May küç.3)'), ('Sahil filialı (Ə.Rəcəbli küç.3)'), 
                                                    ('Xətai filialı (Xocalı pr.37)'), ('Sumqayıt filialı (S.Vurğun küç.102)'),
                                                    ('Mərkəz filialı (B.Sərdarov küç.,1)'), ('Şirvan filialı (20 yanvar küç.12)'),
                                                    ('Kürdəmir filialı (H.Əliyev pr. 3-cü məh. 50)'), ('Ağsu filialı (M.Rəsulzadə küç.35)'),
                                                    ('Şamaxı filialı (N. Nərimanov küç. 66)'), ('Şəki filialı (M.Rəsulzadə küç.178)'), 
                                                    ('Xaçmaz filialı (N.Nərimanov küç.15)'), ('Quba filialı (H.Əliyev pr. və T.Əhmədov küç. kəsişməsi)')])
    Service = SelectField('Select service type', choices=[('Seçin'), ('Kredit müraciəti'), 
                                                          ('Sürətli pul köçürmələri'), ('Plastik kart'), 
                                                          ('Əmanət'), ('Hesab üzrə əməliyyatlar'), 
                                                          ('Hüquqi şəxs və sahibkarlar')])
    Date = DateField('Select date', validators=[DataRequired()], render_kw={"min": "2024-06-01", "max": "2024-07-30"})
    Time = SelectField("Select time",choices=[("09:00:00"),("10:00:00"),
                                              ("11:00:00"),("12:00:00"),
                                              ("13:00:00"),("14:00:00"),
                                              ("15:00:00"),("16:00:00")])
    prefix = SelectField(" ",choices=[("050"),("055"),
                                      ('051'),('099'),
                                      ("070"),('077'),
                                      ('010'),('060')])
    phone = IntegerField(' ',render_kw={'placeholder':'604 19 05'},validators = [DataRequired()])


    