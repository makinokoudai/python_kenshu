import sys
args = sys.argv

# 引数を変数に代入
country_number = int(args[1])-1

# タプルの定義
countyies = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# 入力値に応じて国の出力
print(countyies[country_number], end="")
