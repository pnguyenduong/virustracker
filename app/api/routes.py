from datetime import datetime
from flask import jsonify, Blueprint
from sqlalchemy import and_
from app.models import VirusData
from app.schemas import data_schema
from tools.routes import filter_country_name, filter_date, get_today_date
from tools.data import import_data

api = Blueprint('api', __name__)


@api.route('/')
def today():

    # get today date
    date = get_today_date()

    # get data for today
    data = VirusData.query.filter_by(date=date).all()
    
    # auto download data for new day
    if data is None:
        import_data()
        data = VirusData.query.filter_by(date=date).all()

    return jsonify(data_schema.dump(data))


@api.route('/all')
def all():

    # get everything from database
    data = VirusData.query.all()

    return jsonify(data_schema.dump(data))


@api.route('/<country_name>/all')
def country_all(country_name):

    # filter out the user input
    country_name = filter_country_name(country_name)

    # get data based on country name
    data = VirusData.query.filter_by(name=country_name).all()

    return jsonify(data_schema.dump(data))


@api.route('/<country_name>')
def country_today(country_name):

    # filter out the user input
    country_name = filter_country_name(country_name)

    # get today date
    date = get_today_date()

    # get data based on country name and current day
    data = VirusData.query.filter( and_(VirusData.name == country_name, VirusData.date == date))
    return jsonify(data_schema.dump(data))


@api.route('/<country_name>/<int:year>-<int:month>-<int:day>')
def country_by_date(country_name, year, month, day):

    # filter out the user input
    country_name = filter_country_name(country_name)

    # filter selected date
    date = filter_date(year, month, day)

    # get data based on country name and selected day
    data = VirusData.query.filter( and_(VirusData.name == country_name, VirusData.date == date))
    return jsonify(data_schema.dump(data))


@api.route('/<int:year>-<int:month>-<int:day>')
def by_date(year, month, day):

    # filter selected date
    date = filter_date(year, month, day)

    # get data based on selected date
    data = VirusData.query.filter_by(date=date).all()

    return jsonify(data_schema.dump(data))