from database import session
from tables import Holiday
from datetime import date

holiday = Holiday(
    holi_date = date(2024,1,1),
    holi_text = "お正月"
)

session.add(holiday)
session.commit()