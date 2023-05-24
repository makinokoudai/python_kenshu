class VendingMachine():
    def __init__(self):
        self.goods = {
            "お茶":110,
            "コーヒー":100,
            "ソーダ":160,
            "コーンポタージュ":130
        }

    def print_all_goods(self):
        print(self.goods)

    def insert_price(self):
        while True:
            try:
                self.inserted_price = int(input("投入金額を入力してください"))
                break
            except ValueError:
                print("数字で入力してください")

            

    def start_proc(self):
        self.print_all_goods()
        self.insert_price()

    def main_loop(self):
        self.start_proc()

        while True:
            if self.inserted_price > 10000:
                print("10,000円を超える金額は投入できません。サイド投入金額を入力してください")
                self.insert_price()
                continue
            elif self.inserted_price % 10 != 0:
                print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
                self.insert_price()
                continue
            elif self.inserted_price < min(self.goods.values()):
                print(str(self.inserted_price) + "園では購入できる商品がありません。再度投入金額を入力してください")
                self.insert_price()
                continue


            #商品選択のループ
            while True:
                stuff = input("何を購入しますか(商品名/cancel)")

                if stuff == "cancel":
                    self.return_oturi(self.inserted_price)
                    return
                
                #指定した商品が存在しない場合
                if not stuff in self.goods.keys():
                    print("お選びの商品は用意がありません。再度選んでください")
                    continue
                
                #指定した商品が高すぎて買えない場合
                if self.goods[stuff] > self.inserted_price:
                    print("投入金が不足しています。再度商品を選んでください")
                    continue

                break

            #金額を減らす
            self.inserted_price -= self.goods[stuff]
            print("残金:{0}円".format(self.inserted_price))
            if self.inserted_price < min(self.goods.values()):
               self.return_oturi(self.inserted_price)
               return

            #続けて買うか
            while True:
                flag = input("続けて購入しますか(Y/N)")
                if flag in ("Y","y","yes","Yes"):
                    break
                if flag in ("N","n","No","no"):
                    self.return_oturi(self.inserted_price)
                    return
                

            
    def return_oturi(self,price):
        res = {
            5000:0,
            2000:0,
            1000:0,
            500:0,
            100:0,
            50:0,
            10:0,
            5:0,
            1:0
        }
        
        while price > 0:
            for judge_price in res.keys():
                if price >= judge_price:
                    res[judge_price] += 1
                    price -= judge_price
                    break

        if sum(res.values()):
            print("おつり")
            for kind,amount in res.items():
                if amount:
                    tanni = "玉"
                    if kind >= 1000:tanni = "札"
                    print(str(kind) + "円" + tanni + ":" + str(amount) + "枚")

        return
    
if __name__ == "__main__":
    vend = VendingMachine()
    vend.main_loop()