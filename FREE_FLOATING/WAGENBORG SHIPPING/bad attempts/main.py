import lxml
import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from pprint import pprint

ua = UserAgent()
# print(ua.random)

URL = 'https://www.wagenborg.com/fleetlist'

response = requests.get(URL)
soup = BS(response.text, 'html.parser')

pprint(soup.findAll('a'))


# if __name__ == '__main__':



