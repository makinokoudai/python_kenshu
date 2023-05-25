from datetime import date
from database import session # 1. データベースへの接続
from tables import Attendnum # 2. テーブルの定義
import sys
args = sys.argv

# 引数を変数に代入
date_aqua = args[1]
number_adult = int(args[2])
number_child = int(args[3])

# 入力値(日付)の分割
year, month, today =  date_aqua[:4], date_aqua[4:6], date_aqua[6:]
dt = date(int(year), int(month), int(today))

# seqのカウント
seq = 1
seq_check = session.query(Attendnum).filter_by(entry_date=date_aqua).all()
print(seq_check)
if seq_check != []:
    seq += 1
else:
    pass

# 登録するデータの編集
attendnum = Attendnum(
    entry_date = dt,
    seq = seq,
    adult = number_adult,
    children = number_child
)

# INSERT処理
session.add(attendnum)

# コミット
session.commit()

