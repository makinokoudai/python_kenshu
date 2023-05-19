import sys

# 値下げする商品種別
target_class = sys.argv[1]
# 値下げする値段
price_down = int(sys.argv[2])

# 商品と対応する価格を格納した辞書
item_price  = {
    "リンゴ":80 ,
    "みかん":198,
    "バナナ":150,
    "ビール":360,
    "日本酒":580,
    "ラーメン":380,
    "うどん":128,
    "パスタ":258
    }

# 商品分類を格納した辞書
item_class = {
    "果物類" : ("リンゴ", "みかん", "バナナ"),
    "酒類" :  ("ビール", "日本酒"),
    "麺類" : ("ラーメン", "うどん", "パスタ")
}

# 価格を更新するループ処理
for item in item_class[target_class]:
    new_price = item_price[item] - price_down
    if new_price < 1:
        new_price = 1
    item_price[item] = new_price
    
print(item_price,end="")

