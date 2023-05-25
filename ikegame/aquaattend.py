import sys
from sqlalchemy import Column,Date,Integer
from database import Base,ENGINE,session
from datetime import date
import datetime
from sqlalchemy import desc


class AquaVisitor(Base):
    __tablename__ = "aquavisitor"
    entry_date = Column("entry_date",Date,primary_key=True)
    seq = Column("seq",Integer,primary_key=True)
    adult = Column("adult",Integer)
    child = Column("child",Integer)

    @staticmethod
    def count_seq(dt: date):
        try:
            return session.query(AquaVisitor).filter_by(entry_date = dt).order_by(desc(AquaVisitor.seq)).first().seq
        except AttributeError:
            return 0
    
    @staticmethod
    def convert_date(dt_str: str):
        return date(int(dt_str[:4]), int(dt_str[4:6]), int(dt_str[6:8]))
    
    def add_record(self,dt: str,adult,child):
        ct = self.count_seq(dt_dttm)

    

if __name__ == "__main__":
    #Base.metadata.create_all(bind=ENGINE)
    date_str = "20230101"
    adult = 4
    child = 10

    dt_dttm = AquaVisitor.convert_date(date_str)
    ct = AquaVisitor.count_seq(dt_dttm)

    visitor = AquaVisitor(
        entry_date = dt_dttm,
        seq = ct + 1,
        adult = adult,
        child = child
    )
    session.add(visitor)
    session.commit()

    session.query(AquaVisitor).filter(AquaVisitor.seq == 190)