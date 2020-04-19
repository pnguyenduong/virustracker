from datetime import datetime
from flask import jsonify, Blueprint
from app.models import VirusData
from app.schemas import data_schema
from tools.routes import filter_country_name, filter_date, get_today_date


api = Blueprint('api', __name__)


@api.route('/')
def index():

    # get today date
    date = get_today_date()
    # get data for today
    data = VirusData.query.filter_by(date=date).all()

    return jsonify(data_schema.dump(data))


@api.route('/all')
def all():

    # get everything from database
    data = VirusData.query.all()

    return jsonify(data_schema.dump(data))


@api.route('/<country_name>')
def country(country_name):

    # filter out the user input
    country_name = filter_country_name(country_name)

    # get data based on country name
    data = VirusData.query.filter_by(name=country_name).all()

    return jsonify(data_schema.dump(data))


@api.route('/<int:year>-<int:month>-<int:day>')
def date(year, month, day):

    # filter date
    date = filter_date(year, month, day)

    # get data based on date
    data = VirusData.query.filter_by(date=date).all()

    return jsonify(data_schema.dump(data))