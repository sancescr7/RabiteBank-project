from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from app import app

db = SQLAlchemy(app)
migrate = Migrate(app,db)
admin = Admin(app, name='MyApp', template_mode='bootstrap4')
login_manager = LoginManager()
login_manager.init_app(app)