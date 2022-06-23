import datetime
import re

# data = input('Please enter date of B/L: ')
date_of_bl = '01.06.2022'
print(date_of_bl[4:5], date_of_bl[5:])
# print(datetime.date.today().strftime("%d.%m.%Y"))
# date_of_bl = '31.' + '0' + str(int(date_of_bl[3:5]) - 1) + date_of_bl[5:]
# print(date_of_bl)
# print(int(datetime.date.today().strftime("%m")) - int(re.findall(r'\d{2}.\d{2}.\d{4}', data)[0][3:5]))


# VALID_DATE = re.compile(r'([0-3]\d)\.([0-1]\d)\.(2022)')
#
# date_of_bl = 'simple one'
# while not VALID_DATE.match(date_of_bl):
#     date_of_bl = input('Please enter valid date of B/L: ')
# diff_month = int(datetime.date.today().strftime("%m")) - int(re.search(r'([0-3]\d)\.([0-1]\d)\.(2022)', date_of_bl)[0][3:5])
# print(diff_month)
#     # print(int(re.search(r'([0-3]\d)\.([0-1]\d)\.(2022)', date_of_bl)[0][3:5]))
#     # print(date_of_bl)
