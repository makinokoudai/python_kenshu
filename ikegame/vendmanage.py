import sys
from sqlalchemy import Column, Integer, String
from database import Base, ENGINE, session
from datetime import date
from sqlalchemy import desc
from contextlib import contextmanager 
from vendculc import VendingMachine


#変数クラス
#-----------------
class Id():
    id = Column("id",String(10),primary_key=True)

class Name(Id):
    name = Column("name",String(20))

class Stock(Id):
    stock = Column("stock",Integer)
#-----------------

#テーブルクラス
#~~~~~~~~~~~~~~~~~
class MerchandiseMaster(Base,Name):
    __tablename__ = "mst_merchandise"
    price = Column("price",Integer)

class StockTable(Base,Stock):
    __tablename__ = "tbl_stock"

class MoneyTable(Base):
    __tablename__ = "tbl_money"
    coin_kind = Column("price",Integer,primary_key=True)
    n_coin = Column("number",Integer)

class MessageTable(Base):
    __tablename__ = "tbl_message"
    seq = Column("seq",Integer,primary_key=True)
    message = Column("message",String(100))
    dt = Column("datetime",date)
#~~~~~~~~~~~~~~~~~

class Operation():
    def __init__(self, session) -> None:
        Base.metadata.create_all(bind=ENGINE)
        self.session = session

    def print_all_goods(self):
        goods = self.session.query(MerchandiseMaster).order_by("").all()
