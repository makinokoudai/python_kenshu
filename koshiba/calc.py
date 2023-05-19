import sys
args = sys.argv

# 引数を変数に代入
input1 = args[1]
input2 = args[2]
input3 = args[3]

# 3つの整数の合計値を求める。
output = int(input1) + int(input2) + int(input3)

print(output, end="")