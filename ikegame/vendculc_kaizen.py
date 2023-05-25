class VendingMachine():
    """
    自販機のお釣りを計算するクラス
    """
    def __init__(self):
        self.goods = {
            "お茶": 110,
            "コーヒー": 100,
            "ソーダ": 160,
            "コーンポタージュ": 130
        }

    def print_all_goods(self):
        """
        自販機の中にあるすべての商品と値段を表示する
        """
        print(self.goods)

    def insert_price(self):
        """
        お金を入れる
        """
        # 有効な数字が入力されるまでループ
        # int()で型変換できれば有効であると判断する
        while True:
            try:
                return int(input("投入金額を入力してください"))
                break
            except ValueError:
                print("数字で入力してください")

    def start_proc(self):
        '''
        メインループの最初に行う処理をまとめて記述
        '''
        self.print_all_goods()

    def check_price(self, price):
        # 10000円を超えない
        if price > 10000:
            print("10,000円を超える金額は投入できません。サイド投入金額を入力してください")

        # 1,5円玉は使えない
        elif price % 10 != 0:
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")

        # 最低金額以上である
        elif price < min(self.goods.values()):
            print(
                str(self.inserted_price) +
                "園では購入できる商品がありません。再度投入金額を入力してください")
        else:
            return True

        return False

    def choose_stuff(self, inserted_price: int) -> tuple:
        """
        商品選択をして、残金を返す関数
        続けて購入する場合は(True, 残金)を、
        しない場合は(False, 残金)を返す
        """
        # 商品選択のループ
        while True:
            stuff = input("何を購入しますか(商品名/cancel)")

            if stuff == "cancel":
                return False, inserted_price

            # 指定した商品が存在しない場合
            if stuff not in self.goods.keys():
                print("お選びの商品は用意がありません。再度選んでください")
                continue

            # 指定した商品が高すぎて買えない場合
            if self.goods[stuff] > inserted_price:
                print("投入金が不足しています。再度商品を選んでください")
                continue

            break

        # 金額を減らす
        inserted_price -= self.goods[stuff]
        print("残金:{0}円".format(inserted_price))
        # 金額が最低を下回った場合
        if inserted_price < min(self.goods.values()):
            return False, inserted_price

        # 続けて買うか
        while True:
            flag = input("続けて購入しますか(Y/N)")
            if flag in ("Y", "y", "yes", "Yes"):
                return False, inserted_price
            if flag in ("N", "n", "No", "no"):
                return False, inserted_price

    def main_loop(self):
        """
        メインループ
        """
        self.start_proc()

        while True:
            inserted_price = self.insert_price()
            if self.check_price(inserted_price):
                break

        while True:
            # 返り値がNoneの場合はお釣りを返して終了
            res = self.choose_stuff(inserted_price)
            if not res[0]:
                self.return_oturi(res[1])
                break

    def return_oturi(self, price):
        res = {
            5000: 0,
            2000: 0,
            1000: 0,
            500: 0,
            100: 0,
            50: 0,
            10: 0,
            5: 0,
            1: 0
        }

        while price > 0:
            for judge_price in res.keys():
                if price >= judge_price:
                    res[judge_price] += 1
                    price -= judge_price
                    break

        if sum(res.values()):
            print("おつり")
            for kind, amount in res.items():
                if amount:
                    tanni = "玉"
                    if kind >= 1000:
                        tanni = "札"
                    print(str(kind) + "円" + tanni + ":" + str(amount) + "枚")

        return


if __name__ == "__main__":
    vend = VendingMachine()
    vend.main_loop()
