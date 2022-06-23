import pandas as pd
import re
import datetime

URL = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph' \
      '-usd.en.html '
VALID_DATE = re.compile(r'([0-3]\d)\.([0-1]\d)\.(2022)')


def scrap_rate_of_exchange(date_of_bl=input('Please enter valid date of B/L: ')):
    while not VALID_DATE.match(date_of_bl):
        date_of_bl = input('Please enter VALID date of B/L: ')

    # variable diff_month needed to choose month
    diff_month = int(datetime.date.today().strftime("%m")) - int(
        re.search(r'([0-3]\d)\.([0-1]\d)\.(2022)', date_of_bl)[0][3:5])

    # scrap site www.ecb.europa.eu
    table = pd.read_html(URL)
    values = table[diff_month]
    value_dict = {}

    while True:
        for day in values:
            for value in values[day]:
                if re.search(r"1\.\d{4}", str((format(value, '.4f')))) and not re.search(r'\.0{4}',
                                                                                         str((format(value, '.4f')))):
                    value_dict[int(str((format(value, '.4f')))[:-6])] = float(
                        re.findall(r"1\.\d{4}", str((format(value, '.4f'))))[0])
        try:
            return value_dict[int(date_of_bl[:2])], date_of_bl, int(date_of_bl[:2])
            break
        except:
            print(date_of_bl)
            if date_of_bl[1] == '.':
                date_of_bl = '0' + str(int(date_of_bl[:1])) + date_of_bl[1:]
            elif int(date_of_bl[1]) == 1 and int(date_of_bl[0]) != 3:
                date_of_bl = '31.0' + str(int(date_of_bl[4:5]) - 1) + date_of_bl[5:]
                # values = table[diff_month + 3]
            else:
                date_of_bl = str(int(date_of_bl[:2]) - 1) + date_of_bl[2:]


if __name__ == '__main__':
    print(scrap_rate_of_exchange())
    # print(scrap_rate_of_exchange('22.06.2022')) # 1.0521 - ok
    # print(scrap_rate_of_exchange('01.06.2022')) # 1.0712 - ok
    # print(scrap_rate_of_exchange('11.05.2022')) # 1.0553 - ok (предыдущий месяц)
    # print(scrap_rate_of_exchange('14.04.2022')) # 1.0878 - ok (2 месяца назад)
    # print(scrap_rate_of_exchange('09.03.2022')) # 1.0993 - ok (3 месяца назад)
    # print(scrap_rate_of_exchange('25.06.2022')) # - (если выходной или нет ещё данных)
