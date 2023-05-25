from datetime import date
from database import session # 1. データベースへの接続
from tables import Holiday # 2. テーブルの定義
import sys
args = sys.argv

# 引数を変数に代入
date_aqua = args[1], '%Y%m%d'
number_adult = int(args[2])
number_child = int(args[3])

print(format(date_aqua, '%Y%m%d'))