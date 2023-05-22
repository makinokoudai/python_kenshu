
# 埋め込みコード
import sys
args = sys.argv

# それぞれの数を変数に代入

args_number = len(args)
numbers=[]

for i in range(args_number-1):
    numbers.append(args[i+1])




#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")
        


# 関数に引数を渡す
for i in numbers:
    calcvalue(int(i))

