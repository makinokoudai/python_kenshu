import sys

num = int(sys.argv[1])
sum = 0

# sum が 100未満のとき, 繰り返しnumを足す
while sum < 100:
    sum += num

# sumの値によって出力を制御する
if sum == 100:
    print("Just 100!",end="")
else:
    print("Over!",end="")