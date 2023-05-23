
# メニュー金額の入力
print("お茶 : 110円")
print("コーヒー : 100円")
print("ソーダ : 160円")
print("コーンポタージュ : 130円")
money = int(input("投入金額を入力してください"))

# 1円玉と5円玉の抽出
money_str = str(money)
if money_str[-1] != 0:
    print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
else:
    pass


# 飲み物の定義
drinks = {"お茶" : 110, "コーヒー" : 100, "ソーダ" : 160, "コーンポタージュ" : 130}

# 投入金額に応じた対応
if money >= 100:
    product = input("何を購入しますか (商品名/cancel)")
    if product == "お茶":
        money -= drinks["お茶"]
    elif product == "コーヒー":
        money -= drinks["コーヒー"]
    elif product == "ソーダ":
        money -= drinks["ソーダ"]
    elif product == "コーンポタージュ":
        money -= drinks["コーンポタージュ"]
    elif product == "cancel":
        pass
    else:
        pass

elif money > 10000:
    print("10,000を超える金額は投入できません。再度投入金額を入力してください")

elif money < 100:
    print(f'{money}円では購入できる商品がありません。再度金額を入力してください')

# おつりの計算(5000円札)
if money > 5000:
    money -= 5000
    i_5000 = 1
else:
    i_5000 = 0

# おつりの計算(1000円札)
i_1000 = 0
while money > 1000:
    money -=1000
    i_1000 += 1
else:
    pass

# おつりの計算(500円玉)
if money > 500:
    money -= 500
    i_500 = 1
else:
    i_500 = 0

# おつりの計算(100円玉)
i_100 = 0
while money > 100:
    money -=100
    i_1000 += 1
else:
    pass

# おつりの計算(50円玉)
if money > 50:
    money -= 50
    i_50 = 1
else:
    i_50 = 0

# おつりの計算(10円玉)
i_10 = 0
while money > 10:
    money -=10
    i_1000 += 1
else:
    pass

remainings = [i_5000, i_1000, i_500, i_100, i_50, i_10]

print(remainings)



