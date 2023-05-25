
product_name = {"お茶":110,"コーヒー":100,"ソーダ":160,"コーンポタージュ":130}

buy_frag = False

input_money = int(input("投入金額を入力してください"))

#おつりを計算して表示する処理
def return_money(input_money):
                # 500円で割る処理
            five_hundred_coin = input_money // 500
            input_money -= 500 * five_hundred_coin
            
            # 100円で割る処理
            one_hundred_coin = input_money // 100
            input_money -= 100 * one_hundred_coin
            
            # 50円で割る処理
            fifty_coin = input_money // 50
            input_money -= 50 * fifty_coin
            
            # 10円で割る処理
            ten_coin = input_money // 10
            input_money -= 10 * ten_coin
            
            print("おつり")
            
            if five_hundred_coin != 0:
                print(f"500円玉:{five_hundred_coin}枚")
            
            if one_hundred_coin != 0:
                print(f"100円玉:{one_hundred_coin}枚") 
                
            if fifty_coin != 0:
                print(f"50円玉:{fifty_coin}枚") 
                
            if ten_coin != 0:
                print(f"10円玉:{ten_coin}枚") 
                
            return
    


# 何を購入するかの処理と買い物を続けるか
def display_product(input_money,min_price):
        input_name = input("何を購入しますか(商品名/cancel)")
        input_money -= product_name[input_name]
        if min_price >= input_money:
            return_money(input_money)
            return
        else:
            print(f"残金:{input_money}")
            continue_buy = input("続けて購入しますか(Y/N)")
    
            if continue_buy == "y" or continue_buy == "Y":
                flag_buy(input_money)
            else :
                return_money(input_money)
            
    

def flag_buy(input_money):
    
    # 10000円を超えるときは、再度入力を求める。
    if input_money >= 10000:
        input_money = int(input("10000円を超える金額は投入できません。再度投入金額を入力してください"))
        flag_buy(input_money)
    
    # 1円玉か、5円玉は使用できないようにする処理
    error_coin = input_money % 10
    if 0 < error_coin and error_coin < 10:
        error_coin = int(input("1円玉、5円玉は使用できません。再度投入金額を入力してください。"))
        flag_buy(error_coin)
        
    # 入力された料金が商品の最小料金を上回っているか確認する。
    min_price = list(product_name.values())[0]

    for mykey, myvalue in product_name.items():
        print( mykey + ":" + str(myvalue))
        if min_price > myvalue:
            min_price = myvalue
    
    if min_price >= input_money:
        input_money = int(input(f"{str(input_money)}円では購入できる商品がありません。再度投入金額を入力してください。"))
        flag_buy(input_money)
        
    display_product(input_money,min_price)        
    
        
    
flag_buy(input_money)



    
