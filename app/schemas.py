from .models import VirusData
from app import ma


class DataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VirusData
    
    id = ma.auto_field()
    name = ma.auto_field()
    case_total = ma.auto_field()
    case_today = ma.auto_field()
    case_active = ma.auto_field()
    case_serious = ma.auto_field()
    recovered_total = ma.auto_field()
    death_today = ma.auto_field()
    death_total = ma.auto_field()
    date = ma.auto_field()
 
    
# init marshmallow schema
data_schema = DataSchema()
datas_schema = DataSchema(many=True)


