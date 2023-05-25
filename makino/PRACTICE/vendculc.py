import sys

args = sys.argv

product_name = {"お茶":110,"コーヒ":100,"ソーダ":160,"コーンポタージュ":130}

input_name = ""

# フラグ変数
buy_flag = False
check_conin_Flag = False


# 10000円を超えるときは、再度入力を求める。
def check_bigmoney(input_money):
    input_money = input_money
    if input_money >= 10000:
        input_money = int(input("10000円を超える金額は投入できません。再度投入金額を入力してください"))
        check_bigmoney(input_money)
    else :
        return input_money


# 辞書に入っている最小料金の金額を返す
min_price = list(product_name.values())[0]

for mykey, myvalue in product_name.items():
    print( mykey + ":" + str(myvalue))
    if min_price > myvalue:
        min_price = myvalue
        
        
# 入力された料金が商品の最小料金を上回っているか確認する。
def check_minmoney(input_money):
    # input_money = input_money
    if min_price >= input_money:
        input_money = int(input(f"{str(input_money)}円では購入できる商品がありません。再度投入金額を入力してください。"))
        check_minmoney(input_money)
    else :
        return input_money
        
        
# 1円玉か、5円玉は使用できません。
def check_coin(error_coin):
    error_coin = input_money % 10
    if 0 < error_coin and error_coin < 10:
        error_coin = int(input("1円玉、5円玉は使用できません。再度投入金額を入力してください。"))
        check_coin(error_coin)
    else:
        check_conin_Flag = True
        return error_coin
    

    


def display_product():
    if input_money >= min_price:
        input_name = input("何を購入しますか(商品名/cancel)")





# 実行手順
input_money = int(input("投入金額を入力してください"))

error_coin = input_money % 10

while not buy_flag :
    check_coin(error_coin)
    print(input_money)
    # input_money = check_bigmoney(input_money)
    
    if (check_conin_Flag == True):
        buy_flag = True
    



# input_money = check_coin(error_coin)
# input_money = check_bigmoney(input_money)
# input_money = check_minmoney(input_money)






