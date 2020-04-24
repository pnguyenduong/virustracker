from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler


# initialize extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
sched = BackgroundScheduler(daemon=True)
