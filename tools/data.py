from bs4 import BeautifulSoup
from app.models import VirusData
from app import db
import requests

# download data from worldometers on current day
def scrape_data():
    base_url = 'https://www.worldometers.info/coronavirus/'
    response = requests.get(base_url)
    if response:
        print('Successful')
    else:
        print('There is a problem')
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', id=["main_table_countries_today"])
    table_rows = table.find_all('tr')
    data = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.strip() for i in td]
        data.append(row)
    return data

# filter out unuse contents
def filter_data(data):
    data = data[1:-8]
    data.pop(6)
    return data

# import data into database objects
def import_data():
    virus_data = VirusData()

    # crawling data
    data_scraped = scrape_data()

    # process data
    data = filter_data(data_scraped)

    for row in data:
        virus_data = VirusData(
            name = row[0], 
            case_total = "".join(filter(lambda x: x.isdigit(), row[1])) if row[1] else 0,
            case_today = "".join(filter(lambda x: x.isdigit(), row[2])) if row[2] else 0,
            case_active = "".join(filter(lambda x: x.isdigit(), row[6])) if row[6] else 0,
            case_serious = "".join(filter(lambda x: x.isdigit(), row[7])) if row[7] else 0,
            recovered_total = "".join(filter(lambda x: x.isdigit(), row[5])) if row[5] else 0,
            death_today = "".join(filter(lambda x: x.isdigit(), row[4])) if row[4] else 0,
            death_total = "".join(filter(lambda x: x.isdigit(), row[3])) if row[3] else 0,
        )
        # save each object
        db.session.add(virus_data)
    # close and finish the session
    db.session.commit()

    