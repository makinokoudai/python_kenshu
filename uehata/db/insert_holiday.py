import database
import tables
from datetime import date

holiday = tables.Holiday(
    holi_date = date(2024,1,1),
    holi_text = "お正月"
)

database.session.add(holiday)
database.session.commit()