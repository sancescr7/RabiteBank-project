from extensions import *
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin,current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Emanetler(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    title = db.Column(db.Text,nullable = False)
    muddet = db.Column(db.Integer,nullable = False)
    faiz = db.Column(db.Float, nullable = False)
    valyuta = db.Column(db.String(100),nullable = False)
    image = db.Column(db.String(255),nullable = False)

    def __init__(self,name,title,muddet,faiz,valyuta,image):
        self.name = name
        self.title = title
        self.muddet = muddet
        self.faiz = faiz
        self.valyuta = valyuta
        self.image = image

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False)

    def __init__(self,name) :
        self.name = name
    def save(self):
        db.session.add(self)
        db.session.commit()

class Xeberler(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    title = db.Column(db.Text,nullable = False)    
    data = db.Column(db.String(100),nullable = False)
    catecory =db.Column(db.String(100),nullable = False)
    image = db.Column(db.String(255),nullable = False)

    def __init__(self,name,title,data,catecory,image):
        self.name = name
        self.title = title
        self.data = data
        self.catecory = catecory
        self.image = image

    def save(self):
        db.session.add(self)
        db.session.commit()

class EmanetlerSorgu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Radio = db.Column(db.String(100),nullable = False)
    Name = db.Column(db.String(100),nullable = False)
    Sorname = db.Column(db.String(100),nullable = False)
    Phone = db.Column(db.Integer,unique = False,nullable = False)

    def __init__(self,Radio,Name,Sorname,Phone):
        self.Radio = Radio
        self.Name = Name
        self.Sorname = Sorname
        self.Phone = Phone
        
    def save(self):
        db.session.add(self)
        db.session.commit()


class Scrool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True,nullable=False)
    cash = db.Column(db.Integer, nullable=False)
    gracePeriod = db.Column(db.Integer, nullable=False)
    CardMin = db.Column(db.Integer, nullable=False)
    CardMax = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255),nullable=False)

    def __init__(self,name,cash,gracePeriod,CardMin,CardMax,image_url):
        self.name = name
        self.cash = cash
        self.gracePeriod = gracePeriod
        self.CardMin = CardMin
        self.CardMax = CardMax
        self.image_url = image_url
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Campaniya(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255),nullable=False)
    baslama = db.Column(db.String(100),nullable=False)
    bitme = db.Column(db.String(100),nullable=False)
    category = db.Column(db.String(100),nullable = False)

    def __init__(self,name,date,title,baslama,bitme,image_url,category):
        self.name = name
        self.date = date
        self.title = title
        self.baslama = baslama
        self.bitme = bitme
        self.image_url = image_url
        self.category = category
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Sorgu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Branch = db.Column(db.String(100),nullable = False)
    Service = db.Column(db.String(100),nullable = False)
    Date = db.Column(db.String(100),nullable = False)
    Time = db.Column(db.String(100),nullable = False)
    Phone = db.Column(db.Integer,unique = False,nullable = False)

    def __init__(self,Branch,Service,Date,Time,Phone):
        self.Branch = Branch
        self.Service = Service
        self.Date = Date
        self.Time = Time
        self.Phone = Phone
    def save(self):
        db.session.add(self)
        db.session.commit()


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(MyModelView(Emanetler,db.session))
admin.add_view(MyModelView(Xeberler,db.session))    
admin.add_view(MyModelView(Scrool,db.session))
admin.add_view(MyModelView(Campaniya,db.session))
