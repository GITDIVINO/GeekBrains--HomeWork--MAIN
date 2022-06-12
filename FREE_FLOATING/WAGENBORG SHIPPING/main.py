import lxml
import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

ua = UserAgent()
# print(ua.random)

URL = 'https://www.wagenborg.com/fleetlist'

response = requests.get(URL)
soup = BS(response.text, 'lxml')

print(soup)

# for i in soup:
#     print(soup.a)

# vessel_names = soup.find('a', class_='lh1 font2 c-brand-1 size4 link-style2 size2-m size3-l sizelink')
# print(vessel_names.text)



# if __name__ == '__main__':



