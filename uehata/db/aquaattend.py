from database import session
from aqua_tables import Aquarium
from datetime import date
import sys

dt, adult, child  = sys.argv[1:]
# datetime型に変換
dt = date(int(dt[:4]),int(dt[4:6]),int(dt[6:8]))

# 連番
cnt = 1
# 同じ日付の記録がある化の確認。あれば全て取得。
aquarium_log = session.query(Aquarium.entry_date).filter_by(entry_date=dt).all()
if aquarium_log is not None:
    for _ in aquarium_log:
        cnt += 1

aquarium = Aquarium(
    entry_date = dt,
    seq = cnt,
    adult = int(adult),
    child = int(child),
)

session.add(aquarium)
session.commit()