from bs4 import BeautifulSoup as BP
import re
import requests
import datetime as DT

URL = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/usd.xml'
VALID_DATE = re.compile(r'2022-[0-1]\d-[0-3]\d')

soup = BP(requests.get(URL).text, 'xml')
values = soup.find_all('Obs')[-31:]
dates_lst = [i['TIME_PERIOD'] for i in values]


def scrap_rate_of_exchange(date_of_bl):
    while not VALID_DATE.match(date_of_bl):
        date_of_bl = input('Please enter VALID date of B/L: ')

    while True:
        if date_of_bl in dates_lst:
            for value in values:  # <class 'bs4.element.Tag'>
                if date_of_bl == value['TIME_PERIOD']:
                    return value['OBS_VALUE']
        else:
            date_of_bl = str(DT.datetime.strptime(date_of_bl, '%Y-%m-%d').date() - DT.timedelta(days=1))


