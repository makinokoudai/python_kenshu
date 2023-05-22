import sys
args = sys.argv

# リストを定義
nums = [int(args[1]), int(args[2]), int(args[3])]

#関数を定義
def calcvalue(*nums):
    for num in nums:
        #あまりを算出
        mod = num % 2

        #あまりの値から奇数偶数判定
        if mod != 0:
            print(str(num) + "は奇数")
        else:
            print(str(num) + "は偶数")

calcvalue(int(args[1]), int(args[2]), int(args[3]))