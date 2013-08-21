import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/')#put name of database after /localhost/)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'whilstialonedidcallthyaid'

# add the following to the __init__ file

# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.login import LoginManager
# from flask.ext.openid import OpenID


# db = SQLAlchemy(app)
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

# from app import views, models

