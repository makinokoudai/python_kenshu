from datetime import date

price = {"weekday":
          {"adult":2000,
           "child":1200},
           "weekend":
           {"adult":2400,
           "child":1500}
           }

weekdays = ("Mon","Tue","Wed","Thu","Fri")
weekends = ("Sat","Sun")

#こっからデータベースいじる
from database import session
from tables import Holiday

class AquaHoliday(Holiday):
    def __init__(self):
        super().__init__()

    def is_holiday(self,date):
        holiday = len(session.query(Holiday.holi_date).filter_by(holi_date=date)).all()
        return bool(holiday)

#ここまで

def calc(dt,n_adult,n_child):

    parsed_dt = date(int(dt[:4]), int(dt[4:6]), int(dt[6:8]))
    day_of_week = parsed_dt.strftime("%a")

    hol = AquaHoliday()
    is_holiday = hol.is_holiday(parsed_dt)

    if day_of_week in weekends or is_holiday:
        return int(n_adult) * price["weekend"]["adult"] + int(n_child) * price["weekend"]["child"]
    
    elif day_of_week in weekdays:
        return int(n_adult) * price["weekday"]["adult"] + int(n_child) * price["weekday"]["child"]
    
if __name__ == "__main__":
    print(calc("20230102","1","10"))
    