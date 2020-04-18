import os


class Config:
    # setting app secret key

    SECRET_KEY = os.environ.get('SECRET_KEY') 

    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # app conflicts in console for SQLALCHEMY_TRACK_MODIFICATIONS
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    