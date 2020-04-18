from flask import jsonify, Blueprint
from datetime import datetime
from ..models import VirusData
from ..schemas import DataSchema

api = Blueprint('api', __name__)

@api.route('/')
def index():

    data = VirusData.query.filter(VirusData.date == datetime.today().date()).all()

    # init marshmallow schema
    data_schema = DataSchema(many=True)
    countries = data_schema.dump(data)

    return jsonify(countries)