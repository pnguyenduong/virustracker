from datetime import datetime
from app import db


class VirusData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    case_total = db.Column(db.Integer)
    case_today = db.Column(db.Integer)
    case_active = db.Column(db.Integer)
    case_serious = db.Column(db.Integer)
    recovered_total = db.Column(db.Integer)
    death_today = db.Column(db.Integer)
    death_total = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'''ID:{self.id}, Country: {self.name}, Total Cases: {self.case_total}, Today Cases: {self.case_today},Active Case: {self.case_active}, Serious: {self.case_serious}, Recovered: {self.recovered_total},Today Deaths: {self.death_today}, Total Deaths: {self.death_total}, Date: {self.date}'\n'''

