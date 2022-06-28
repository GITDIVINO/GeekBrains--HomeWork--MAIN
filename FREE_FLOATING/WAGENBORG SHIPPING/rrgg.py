import time
import datetime as DT

date_of_bl = '2022-06-01'

date = DT.datetime.strptime(date_of_bl, '%Y-%m-%d').date()
print(date, type(date))
date -= DT.timedelta(days=1)
print(date, type(date), str(date))
