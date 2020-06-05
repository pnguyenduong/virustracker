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
            name = row[1], 
            case_total = 0 if not row[2] else "".join(filter(lambda x: x.isdigit(), row[2])),
            case_today = 0 if not row[3] else "".join(filter(lambda x: x.isdigit(), row[3])),
            death_today = 0 if not row[5] else "".join(filter(lambda x: x.isdigit(), row[5])),
            death_total = 0 if not row[4] else "".join(filter(lambda x: x.isdigit(), row[4])),
            recovered_total = 0 if not row[6] or row[6] == "N/A" else "".join(filter(lambda x: x.isdigit(), row[6])),
            
        )
        # save each object
        db.session.add(virus_data)
    # close and finish the session
    db.session.commit()

    