from datetime import date
import sys
args = sys.argv

# 引数を変数に代入
date_aqua = int(args[1])
number_adult = int(args[2])
number_child = int(args[3])

today = date_aqua % 100
month = int(((date_aqua - today) % 10000) / 100)
year = int((date_aqua - month - today) / 10000)

# print(today)
# print(month)
# print(year)

dt = date(year, month, today)

day_of_week = dt.strftime("%a")
print(day_of_week)
if day_of_week == "Sat" or day_of_week == "Sun":
    fee_adult = 2400
    fee_child = 1500
else:
    fee_adult = 2000
    fee_child = 1200

fee_total = fee_adult * number_adult + fee_child * number_child
print(fee_total, end="")