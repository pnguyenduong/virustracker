from datetime import datetime
import pycountry

# filter country name in route inputs
def filter_country_name(country_name):
    if country_name == 'usa' or country_name == 'uk':
        return country_name.upper()
    elif country_name == 'vn':
        return 'Vietnam'
    country = pycountry.countries.get(alpha_2=country_name.upper())
    return country.name

# filter date in route inputs
def filter_date(year, month, day): 
    return f'{year}-{month}-{day}'

# get today date
def get_today_date():
    return datetime.today().date()



