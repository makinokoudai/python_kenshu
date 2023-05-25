# メニュー金額の入力
print("お茶 : 110円")
print("コーヒー : 100円")
print("ソーダ : 160円")
print("コーンポタージュ : 130円")
print("投入金額を入力してください")
money = int(input())

# 飲み物の定義
drinks = {"お茶" : 110, "コーヒー" : 100, "ソーダ" : 160, "コーンポタージュ" : 130}

# 10000万円以上または購入不可金額または1円玉と5円玉があれば再度金額入力
while money > 10000 or money < 100 or money % 10 != 0:
    if money > 10000:
        print("10,000円を超える金額は投入できません。再度金額を入力してください。")
    elif money < 100:
        print(f'{money}円では購入できる商品がありません。再度金額を入力してください。')
    elif money % 10 != 0:
        print('1円玉、5円玉は使用できません。再度投入金額を入力してください。')
    money = int(input())
else:
    pass

# 購入案内
print("何を購入しますか (商品名/cancel)")
product = input()

if product == "cancel":
    pass
else:
    while money < drinks[product]:
        print(f'{money}円では購入できる商品がありません。再度商品名を入力してください。')
        product = input()
    else:
        money -= drinks[product]

# 残金表示
print(f'残金 : {money}円')

# 追加購入の案内
while money >= 100: # 100円以下ならパス
    print("続けて購入しますか (Y/N)")
    YN = input()
    if YN == "Y": # Nならパス
        if product == "cancel": # cancelしたらパス
            pass
        else:
            print("何を購入しますか (商品名/cancel)")
            product = input()
            while money < drinks[product]: # 購入不可なら再度商品名入力
                print("再度商品名を入力してください。")
                product = input()
                if product == "cancel": # cancelしたらパス
                    break
                else:
                    pass
            else:
                money -= drinks[product]
                print(f'残金 : {money}円')
    else : 
        break
else:
    pass


# おつりの計算(5000円札)
if money >= 5000:
    money -= 5000
    i_5000 = 1
else:
    i_5000 = 0

# おつりの計算(1000円札)
i_1000 = 0
while money >= 1000:
    money -=1000
    i_1000 += 1
else:
    pass

# おつりの計算(500円玉)
if money >= 500:
    money -= 500
    i_500 = 1
else:
    i_500 = 0

# おつりの計算(100円玉)
i_100 = 0
while money >= 100:
    money -=100
    i_100 += 1
else:
    pass

# おつりの計算(50円玉)
if money >= 50:
    money -= 50
    i_50 = 1
else:
    i_50 = 0

# おつりの計算(10円玉)
i_10 = 0
while money >= 10:
    money -=10
    i_10 += 1
else:
    pass

remainings = [i_5000, i_1000, i_500, i_100, i_50, i_10]

print(f'おつり : {money}円')
print(f"5000円札 : {remainings[0]}枚")
print(f"1000円札 : {remainings[1]}枚")
print(f"500円玉 : {remainings[2]}枚")
print(f"100円玉 : {remainings[3]}枚")
print(f"50円玉 : {remainings[4]}枚")
print(f"10円玉 : {remainings[5]}枚")





