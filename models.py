from extensions import *

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

admin.add_view(ModelView(Scrool,db.session))
admin.add_view(ModelView(Campaniya,db.session))