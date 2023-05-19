import sys
args = sys.argv

# 引数を変数に代入
type = args[1]
price_reduction = int(args[2])

# 辞書型で定義
foods = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

# 値下げ
if type == "果物類":
        foods["リンゴ"] -= price_reduction
        foods["みかん"] -= price_reduction
        foods["バナナ"] -= price_reduction
        if foods["リンゴ"] <= 0:
               foods["リンゴ"] = 1
        else:
               pass
        if foods["みかん"] <= 0:
               foods["みかん"] = 1
        else:
               pass
        if foods["バナナ"] <= 0:
               foods["バナナ"] = 1
        else:
               pass
elif type == "酒類":
        foods["ビール"] -= price_reduction
        foods["日本酒"] -= price_reduction
        if foods["ビール"] <= 0:
               foods["ビール"] = 1
        elif foods["日本酒"] <= 0:
               foods["日本酒"] = 1
        else:
               pass
elif type == '麺類':
        foods["ラーメン"] -= price_reduction
        foods["うどん"] -= price_reduction
        foods["パスタ"] -= price_reduction
        if foods["ラーメン"] <= 0:
               foods["ラーメン"] = 1
        elif foods["うどん"] <= 0:
               foods["うどん"] = 1
        elif foods["パスタ"] <= 0:
               foods["パスタ"] = 1
        else:
               pass
else:
    print("error")

# 0円以下のものを1円にする。

print(foods, end="")




