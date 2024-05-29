from extensions import *
from flask_admin.contrib.sqla import ModelView

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

admin.add_view(ModelView(Emanetler,db.session))
admin.add_view(ModelView(Xeberler,db.session))