from datetime import date
from database import session # 1. データベースへの接続
from tables import Holiday # 2. テーブルの定義
import sys
args = sys.argv

# 引数を変数に代入
date_aqua = args[1]
number_adult = int(args[2])
number_child = int(args[3])

# 入力値(日付)の分割
year, month, today =  date_aqua[:4], date_aqua[4:6], date_aqua[6:]
dt = date(int(year), int(month), int(today))

# 日付の取得
day_of_week = dt.strftime("%a")

# データベースからデータを取得
holiday = session.query(Holiday).filter_by(holi_date=date_aqua).all()

if day_of_week == "Sat" or day_of_week == "Sun" or holiday != []:
    fee_adult = 2400
    fee_child = 1500
else:
    fee_adult = 2000
    fee_child = 1200

fee_total = fee_adult * number_adult + fee_child * number_child
print(fee_total, end="")