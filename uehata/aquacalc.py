import sys
from datetime import date

# コマンドライン引数の分割代入
dt, adult, child  = sys.argv[1:]
# datetime型に変換
dt = date(int(dt[:4]),int(dt[4:6]),int(dt[6:8]))
# 入力された日付の曜日を算出
weekday = dt.strftime("%a")

adult_fee = 2000
child_fee = 1200
sum_fee = 0

if weekday == "Sat" or weekday == "Sun":
    # 休日は料金を更新する
    adult_fee = 2400
    child_fee = 1500
    # 合計料金の計算
    sum_fee += adult_fee * int(adult)
    sum_fee += child_fee * int(child)
else:
    # 平日の処理
    sum_fee += adult_fee * int(adult)
    sum_fee += child_fee * int(child)
    
print(sum_fee,end="")