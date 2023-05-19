import sys
args = sys.argv

# 引数を変数に代入
number_unit = int(args[1])

# 合計値を定義。ここに数字をどんどん足す。
number_amount = 0

# 足し算の繰り返し、条件別で出力変更。
while number_amount < 100:
    number_amount += number_unit
else:
    if number_amount == 100:
        print('Just 100!', end="")
    else:
        print('Over!', end="")