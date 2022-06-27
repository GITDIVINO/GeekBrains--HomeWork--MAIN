from bs4 import BeautifulSoup as BP
import re
import requests

URL = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/usd.xml'
VALID_DATE = re.compile(r'2022-[0-1]\d-[0-3]\d')

soup = BP(requests.get(URL).text, 'xml')
values = soup.find_all('Obs')[-31:]


def scrap_rate_of_exchange(date_of_bl):
    while not VALID_DATE.match(date_of_bl):
        date_of_bl = input('Please enter VALID date of B/L: ')

    for value in values:  # <class 'bs4.element.Tag'>
        if date_of_bl == value['TIME_PERIOD']:
            return value['OBS_VALUE']


if __name__ == '__main__':
    print(scrap_rate_of_exchange(input('Please enter valid date of B/L: ')))
