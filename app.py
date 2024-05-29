# from flask import Flask 

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:123456@127.0.0.1:3306/mydb'
# app.config["SECRET_KEY"] = 'OUR_PROJECT'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# # app.config["SQLALCHEMY_ECHO"] = True


# # SQLALCHEMY_TRACK_MODIFICATION = True

# from extensions import *
# from controller import *
# from models import *


# if __name__ =='_main_':
#     app.init_app(db)
#     app.init_app(migrate)
#     app.run(port=5000,debug=True)

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
    app.run(port = 5000,debug = True)
