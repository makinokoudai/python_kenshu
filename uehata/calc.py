import sys
# コマンドライン引数の受け取り(str[])
num = sys.argv[1:]

# numから要素を1つずつ取り出してstr -> intに変換
# sum に足し合わせる
sum = 0
for i in num :  sum += int(i) 
print(sum, end="")