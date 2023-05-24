from database import session
from aqua_tables import Aquarium
from datetime import date
import sys

dt, adult, child  = sys.argv[1:]
# datetime型に変換
dt = date(int(dt[:4]),int(dt[4:6]),int(dt[6:8]))

# 同じ日付の記録があるかの確認。あれば全て取得。
aquarium_log = session.query(Aquarium.entry_date).filter_by(entry_date=dt).all()
seq = len(aquarium_log) + 1

# 登録用データの作成
aquarium = Aquarium(
    entry_date = dt,
    seq = seq,
    adult = int(adult),
    child = int(child),
)

session.add(aquarium)
session.commit()