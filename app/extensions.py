from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# initiate extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()