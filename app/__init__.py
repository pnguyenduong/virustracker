from flask import Flask, jsonify
from configs import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# initiate and configuring the app
app = Flask(__name__)
app.config.from_object(Config)

    
# initiate extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.models import VirusData
from app.schemas import DataSchema
from app.routes import *





    

