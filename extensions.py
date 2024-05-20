from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app

db = SQLAlchemy(app)
migrate = Migrate(app,db)
admin = Admin(app)