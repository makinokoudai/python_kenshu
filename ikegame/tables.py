import sys
from sqlalchemy import Column, String, Date, Integer
from database import Base,ENGINE

class Holiday(Base):
    __tablename__ = "holiday"
    holi_date = Column("holi_date",Date,primary_key=True)
    holi_text = Column("holi_text",String(20))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__=="__main__":
    main(sys.argv)