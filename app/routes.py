from flask import jsonify
from datetime import datetime
from app.models import VirusData
from app.schemas import DataSchema
from app import app

@app.route('/')
def index():

    data = VirusData.query.filter(VirusData.date == datetime.today().date()).all()

    # init marshmallow schema
    data_schema = DataSchema(many=True)
    countries = data_schema.dump(data)

    return jsonify(countries)