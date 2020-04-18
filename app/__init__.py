from flask import Flask
from configs.settings import Config
from .extensions import db, ma

def create_app(config_class=Config):

    # initiate and configuring the app
    app = Flask(__name__)
    app.config.from_object(Config)

    # initiate extensions
    db.init_app(app)
    ma.init_app(app)    

    # importing blueprint packages
    from app.api.routes import api

    # register blueprint app for ready to use
    app.register_blueprint(api)

    # import variable for flask shell
    from app.models import VirusData
    from app.api.tools import scrape_data, filter_data, import_data
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'VirusData': VirusData, 'scrape_data': scrape_data,
                'filter_data': filter_data, 'import_data': import_data}

    return app






    

