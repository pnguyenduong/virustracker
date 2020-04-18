from flask import jsonify, Blueprint
from datetime import datetime
from ..models import VirusData
from ..schemas import data_schema

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

    if name.islower() == True:
        name = name.capitalize()
        print(name)
    data = VirusData.query.filter_by(name=name).all()

    return jsonify(data_schema.dump(data))