def calc_change(items, num, min_val):
    # 10000円を超える金額が投入された場合の処理
    if num >= 10001:
        new_num = int(input("10,000円を超える金額は投入できません。再度投入金額を入力してください"))
        calc_change(new_num,min_val)
        return 
    
    # 1円玉、5円玉が投入された場合の処理
    if str(num)[-1] != "0":
        new_num =  int(input("1円玉、5円玉は使用できません。再度投入金額を入力してください"))
        calc_change(new_num,min_val)
        return
    
    if num >= min_val:
        item = input("何を購入しますか（商品名/cancel)")
        
        # TODO : キャンセルの場合の処理
        if item == "cancel":
            print("cancel")
            pass
        
        remain_money = num - items[item]
        
        # 残金が0になった場合の処理
        if remain_money == 0:
            return
        print(f"残金：{remain_money}円")
        res = input("続けて購入しますか( Y/N )")
        
        # TODO: おつり計算の処理
        if res == "N":
            pass
        
        elif res == "Y":
            pass
        
        else:
            pass
        
    else:
        # 投入金額よりも商品の値段が低い場合の処理
        new_num = int(input(f"{num}円では購入できる金額がありません。再度投入金額を入力してください"))
        calc_change(new_num,min_val)
        return

if __name__ == "__main__":
    item_dict = {
        "お茶" : 110,
        "コーヒー" : 100,
        "ソーダ" : 160,
        "コーンポタージュ" : 130,
    }
    
    for k, v in item_dict.items():
        print(f"{k} : {v}円")

    num = int(input("投入金額を入力してください"))

    min_val = min(item_dict.values())

    calc_change(item_dict,num, min_val)


