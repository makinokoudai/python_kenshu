import sys
args = sys.argv

# 引数を変数に代入
first_station_name = args[1]
last_station_name = args[2]

# 辞書の定義
shinkansen_stations = {'東京' : 0.00, '品川' : 6.78, '新横浜' : 25.54, '名古屋' : 342.02, '京都' : 476.31, '新大阪' : 515.35}

try:
    # キーから値に変換、小数第二位までの数値にする
    first_station = shinkansen_stations[first_station_name]
    last_station = shinkansen_stations[last_station_name]

    # 距離の算出
    distance = abs(last_station - first_station)

    # 出力
    print(round(distance,2), end="")

except:
    print('のぞみの停車駅を引数に設定してください', end="")


