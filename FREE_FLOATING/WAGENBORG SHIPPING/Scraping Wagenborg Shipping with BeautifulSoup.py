""""
This program should find data of vessel which owened by Wagenborg Shipping
"""

from bs4 import BeautifulSoup
import requests

URL = 'https://www.wagenborg.com/ships/adamas'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')  # data parced from site in html

vessel_name = soup.find('h1', class_='size5 size6-m size7-l mb mb2-l lh1 font2')    # looking for name of the vessel
print(f'Name of the vessel: {vessel_name.text}\n')

label_lst = [data_label.text for data_label in soup.find_all('td', class_='table-row__label')]
data_lst = [data_text.text for data_text in soup.find_all('td', class_='table-row__text')]

# combine two lists
for data in dict(zip(label_lst, data_lst)).items():
    print(data)
