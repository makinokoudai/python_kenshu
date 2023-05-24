from datetime import date
import sys

day = sys.argv[1]
adult_num = int(sys.argv[2])
child_num = int(sys.argv[3])

get_year = 0
get_mon = 0
get_day =0  

get_year = int(day[0:4])
get_mon = int(day[4:6])
get_day = int(day[6:8])


dt = date(get_year,get_mon,get_day)
week = dt.strftime("%a")


def calcsum(week,adult_num,child_num):
    if week == "Sat" or week == "Sun":
        adult_money = 2400
        child_money = 1500
        sum = adult_num * adult_money + child_num * child_money
        return sum
    else:
        adult_money = 2000
        child_money = 1200
        sum = adult_num * adult_money + child_num * child_money
        return sum 
        
    
print(calcsum(week,adult_num,child_num),end="")


