import sys
try : 
    food = sys.argv[1]
    print(f"I don't like {food}", end="")

# コマンドライン引数が空のとき
except IndexError :
    print("エラー : 食べ物を1つ入力してください",end="")
