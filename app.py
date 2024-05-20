from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3308/moviesdb'
app.config['SECRET_KEY'] = 'our_project'
SQLALCHEMY_TRACK_MODIFICATIONS = True
from extensions import *
from controlers import *
from models import *
if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    # if not Scrool.query.first():
    #     test_user = Scrool(name='Yaşıl keşbek',
    #                        cash:100,
    #                        gracePeriod:100,
    #                        CardMin:200,
    #                        CardMax:15 000,
    #                        image_url='https://www.rabitabank.com/resized/resize880/center/pages/5/kredit-sayt-banner.png')
    #     test_user.save()
    app.run(port = 5000,debug = True)