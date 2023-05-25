"""
# 自動販売機のおつり計算プログラム

[条件]
* cencelと入力されたとき、おつりを計算して処理を終了する
* 10,000円を超える金額が入力されたとき、再度投入金額を問う
* 投入金額では何も買えないとき、再度投入金額を問う
* 1の位が0以外の場合には再度投入金額を問う
* 残金がちょうど0の場合にはメッセージを出力することなく終了する
* 残金がある場合Y/Nの入力に対応した処理を返す
* おつりは5000円・2000円・1000円・500円・100円・50円・10円の大きい順に割り当てて返却する


"""

def calc_vend_change(item_price):
    '''
    
    * 機能 : 自販機のおつりを計算する
    * 入力 : 商品とその値段(dict)
    * 出力 : None
    * 内部関数 : 
        1. _validate_input() : バリデーション
        2. _purchase()       : 商品の購入処理
        3. _calc_change      : おつりの計算
        
    '''    
    min_val = min(list(item_price.values()))
    def _validate_input(money,min_price=min_val):
        '''
        * 機能 : 投入金額のバリデーションを行う。
        * 入力 : 
            1. money      : 投入金額 (int)
            2. min_price  : 商品の最安値 (int)
        * 出力 : 投入金額 (int)
        * 補足 : 再起呼び出し
        
        '''
        # 条件1 : 投入金額が10000円以下
        if money > 10000:
            OVER_MONEY_TEXT = "10,000円を超える金額は投入できません。再度投入金額を入力してください"
            new_money = int(input(OVER_MONEY_TEXT))
            _validate_input(new_money)
        
        # 条件2 : 投入金額が商品の最低金額以上
        if money < min_price:
            not_enough_text = f"{money}円では購入できる商品がありません。再度投入金額を入力してください"
            new_money = int(input(not_enough_text))
            _validate_input(new_money)
        
        # 条件3 : 投入金額の1の位が0以外
        if str(money)[-1] != "0":
            INVALID_TEXT = "1円玉、5円玉は使用できません。再度投入金額を入力してください"
            new_money = int(input(INVALID_TEXT))
            _validate_input(new_money)

        return money
    
    def _purchase(change, item_price=item_price, min_price=min_val):
        '''
        * 機能 : 商品購入部分の処理
        * 入力 : 
            1. change     : 残金 (int)
            2. item_price : 商品とその値段 (dict) 
            3. min_price  : 商品の最安値 (int)
        * 出力 : None or 残金(int)
        * 補足 : 再帰呼び出し
        
        '''
        ASK_PURCHASE_TEXT = "何を購入しますか（商品名/cancel)"
        item_name = input(ASK_PURCHASE_TEXT) 
        
        # cancelが入力されたとき、残金を返す
        if item_name == "cancel" or item_name == "c":
            return change
        
        # 残金の計算
        new_change = change - item_price[item_name]
        
        # 残金がちょうど0円のとき
        if new_change == 0:
            return None
        
        # 残金が最安値より小さいとき
        if new_change < min_price:
            return new_change
        
        # 残金の表示
        change_text = f"残金：{new_change}円"
        print(change_text)
        
        # 購入を継続するか。
        # Yなら再帰呼び出し。Nなら残金を返す。 それ以外なら再度質問をする。
        flag = True
        while flag:
            
            IS_CONTINUE_TEXT = "続けて購入しますか(Y/N)"
            is_continue = input(IS_CONTINUE_TEXT)
            
            # 購入を継続するとき、再帰呼び出し
            if is_continue == 'Y' or is_continue == "y":
                flag = False
                _purchase(new_change)
            # 継続しないとき、残金を返す
            elif is_continue == 'N' or is_continue == "n":
                flag = False
                return new_change
            else:
                pass 

    def _calc_change(change):
        '''
        * 機能 : 残金からおつりを計算する
        * 入力 : 
            1. change     : 残金 (int)
        * 出力 : None        
        
        ''' 
        print("おつり")
    
        # おつりの構成要素
        jpy = (5000, 2000, 1000, 500, 100, 50, 10)
        
        # 残金からおつりを計算してchange_listに格納
        change_list = []
        for i in jpy:
            if change >= i :
                num =  change // i
                change_list.append((i, num))
                change -= i * num
        
        
        # おつりの出力
        for pay in change_list:
            if len(str(pay[0])) >= 4:
                print(f"{pay[0]}円札：{pay[1]}枚")
            else:
                print(f"{pay[0]}円玉：{pay[1]}枚")
    
    
    # 商品とその値段を出力
    for k, v in item_price.items():
        print(f"{k} : {v}円")
        
    # 初回の金額の受け取り
    INPUT_TEXT = "投入金額を入力してください"
    money = int(input(INPUT_TEXT))
    # 投入金額のバリデーション
    is_valid_money = _validate_input(money, min_val)
    # 金額に応じた購入処理
    change = _purchase(is_valid_money)
    
    # おつりがない場合は何も表示せず終了
    if change is None:
        return 
    else:
        # おつりの計算
        _calc_change(change) 
        
if __name__ == "__main__":
    item_price_dict = {
        "お茶" : 110,
        "コーヒー" : 100,
        "ソーダ" : 160,
        "コーンポタージュ" : 130,
    }
    calc_vend_change(item_price_dict)