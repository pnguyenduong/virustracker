from flask import jsonify, Blueprint
from datetime import datetime
from ..models import VirusData
from ..schemas import data_schema
from .tools import filter_input
api = Blueprint('api', __name__)

@api.route('/')
def index():

    data = VirusData.query.filter(VirusData.date == datetime.today().date()).all()

    return jsonify(data_schema.dump(data))

@api.route('/all')
def all():

    data = VirusData.query.all()

    return jsonify(data_schema.dump(data))


@api.route('/<name>')
def country(name):

    # filter out the user input
    name = filter_input(name)
    
    data = VirusData.query.filter_by(name=name).all()

    return jsonify(data_schema.dump(data))