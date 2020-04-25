from flask import Flask
from configs.settings import Config
from .extensions import db, ma, migrate, sched


def create_app(config_class=Config):

    # initiate and configuring the app
    app = Flask(__name__)
    app.config.from_object(Config)

    # initiate extensions
    db.init_app(app)
    ma.init_app(app)    
    migrate.init_app(app, db)    

    # importing blueprint packages
    from app.api.routes import api
    from app.errors.error_handlers import errors

    # register blueprint app for ready to use
    app.register_blueprint(api)
    app.register_blueprint(errors)

    # import variables ready to use for flask shell
    from app.models import VirusData
    from tools.data import scrape_data, filter_data, import_data
    
    # setting up the variables in flask shell
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'VirusData': VirusData, 'scrape_data': scrape_data,
                'filter_data': filter_data, 'import_data': import_data}

    # setting up background job
    sched.add_job(import_data, 'cron', day='*', hour='0')
    sched.start()

    return app






    

