import sys
args = sys.argv

# 引数を変数に代入
food_type = args[1]
price_reduction = int(args[2])

# カテゴリ:商品群に定義して、更に商品:値段で定義
foods = {"果物類" : {"リンゴ":80 , "みかん":198, "バナナ":150}, "酒類" : {"ビール":360, "日本酒":580}, "麺類" : {"ラーメン":380, "うどん":128, "パスタ":258}}


# 値下げ処理(0円以下の場合は1円とする)

for i in foods[food_type]:
        foods[food_type][i] -= price_reduction
        if foods[food_type][i] <= 0:
               foods[food_type][i] = 1
        else:
               pass
 
# 出力
print(foods, end="")
