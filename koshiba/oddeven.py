import sys
args = sys.argv

# 引数を変数に代入
number = int(args[1])

# 偶奇判定
if number % 2 == 1:
    print("奇数", end="")
else:
    print("偶数", end="")