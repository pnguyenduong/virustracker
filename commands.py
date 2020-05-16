import click
from flask.cli import with_appcontext
from app import db
from tools.data import scrape_data, filter_data, import_data

@click.command(name='create_table')
@with_appcontext
def create_table():
    db.create_all()


@click.command(name='import_data_from_server')
@with_appcontext
def import_data_from_server():
    import_data()

