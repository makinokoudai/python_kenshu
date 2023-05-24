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

def calc(dt,n_adult,n_child):

    parsed_dt = date(int(dt[:4]), int(dt[4:6]), int(dt[6:8]))
    day_of_week = parsed_dt.strftime("%a")

    if day_of_week in weekdays:
        return int(n_adult) * price["weekday"]["adult"] + int(n_child) * price["weekday"]["child"]
    elif day_of_week in weekends:
        return int(n_adult) * price["weekend"]["adult"] + int(n_child) * price["weekend"]["child"]
    
if __name__ == "__main__":
    import sys
    args = sys.argv
    print(calc(*args[1:]), end="")
    