import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    # setting app secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') 

    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data-dev.db')
    # app conflicts in console for SQLALCHEMY_TRACK_MODIFICATIONS
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    