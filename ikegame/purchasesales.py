import sys
from sqlalchemy import Column, Integer, String
from database import Base, ENGINE, session
from datetime import date
from sqlalchemy import desc
from contextlib import contextmanager 


#変数クラス
#-----------------
class Id():
    id = Column("id",String(10),primary_key=True)

class Hinmoku(Id):
    name = Column("name",String(20))
#-----------------

#テーブルクラス
#~~~~~~~~~~~~~~~~~
class HinmokuMaster(Base,Hinmoku):
    __tablename__ = "mst_hinmoku"

class Zaiko(Base,Id):
    __tablename__ = "tbl_zaiko"
    unit = Column("unit",String(10),primary_key=True)
    unitprice = Column("unitprice",Integer,primary_key=True)
    stock = Column("stock",Integer)
#~~~~~~~~~~~~~~~~~

class OperationProc():
    def __init__(self,session) -> None:
        self.session = session

    def check_hinmoku(self,id):
        '''品目マスタに品目が既に存在する場合はTrue,しない場合はFalseを返す'''
        return bool(self.session.query(HinmokuMaster).filter(HinmokuMaster.id == id).count())
    
    @contextmanager
    def proc(self):
        yield
        self.session.commit()
    
    def add_hinmoku(self,id,name,**kwargs):
        if self.check_hinmoku(id):
            print("品目マスタに" + id + "は登録済みです")
        else:
            hinmoku = HinmokuMaster(
                id = id,
                name = name
            )
            self.session.add(hinmoku)
        
    def add_siire(self,id,unit,unitprice,stock_diff,**kwargs):
        zaiko = self.session.query(Zaiko).filter_by(id=id).first()
        if zaiko:
            #単位チェック
            assert unit == zaiko.unit
            assert unitprice == zaiko.unitprice
            zaiko.stock += stock_diff

        else:
            new_zaiko = Zaiko(
                id = id,
                unit = unit,
                unitprice = unitprice,
                stock = stock_diff
            )
            self.session.add(new_zaiko)

        print("品目{id}(単価: {unitprice}円)を{stock}{unit}仕入れました".format(id=id,unitprice=unitprice,stock=stock_diff,unit=unit))


    def add_uriage(self,id,stock_diff,**kwargs):
        '''売上を登録 - 在庫を減らす処理をする'''
        zaiko = self.session.query(Zaiko).filter(Zaiko.id==id).first()
        assert zaiko

        if zaiko.stock < stock_diff:
            print("売上数量に対して在庫が足りません。在庫を確認してください")
            return
        
        zaiko.stock -= stock_diff
        unitprice = self.session.query(Zaiko).filter_by(id=id).first().unitprice
        unit = self.session.query(Zaiko).filter_by(id=id).first().unit
        
        print("品目{id}(単価: {unitprice}円)を{kosuu}{unit}売上ました".format(id=id,unitprice=unitprice,kosuu=stock_diff,unit=unit))

    def zaiko_out(self):
        zaiko_list = self.session.query(Zaiko).order_by(Zaiko.id).all()
        for zaiko in zaiko_list:
            print("品目{id}({name})の在庫: {stock}{unit}(単価: {unitprice}円)".format(
                id = zaiko.id,
                name = self.session.query(HinmokuMaster).filter_by(id=zaiko.id).first().name,
                stock = zaiko.stock,
                unit = zaiko.unit,
                unitprice = zaiko.unitprice
            ))
        


class Operation():
    def __init__(self,session):
        Base.metadata.create_all(bind=ENGINE)
        self.session = session

    def parse_args(self,*args):
        mode = args[0]
        res = {}
        if mode == "1":
            res["id"] = args[1]
            res["name"] = args[2]
        elif mode in  ("2","3"):
            res["id"] = args[1]
            res["unit"] = args[2]
            res["unitprice"] = int(args[3])
            res["stock_diff"] = int(args[4])
        elif mode == "4":
            pass

        return mode,res
    

    def operate(self,*args):
        mode,args_dict = self.parse_args(*args)
        opp = OperationProc(self.session)

        if mode == "1":
            with opp.proc():
                opp.add_hinmoku
        elif mode == "2":
            with opp.proc():
                opp.add_siire
        elif mode == "3":
            with opp.proc():
                opp.add_uriage
        elif mode == "4":
            opp.zaiko_out()
        else:
            print("有効な処理モードを入力してください")
            return



def main(args):
    op = Operation(session = session)
    op.operate(*args[1:])

if __name__=="__main__":
    main(sys.argv)

