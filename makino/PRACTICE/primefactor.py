import sys
import math

number = int(sys.argv[1])

# 素数かどうかをチェック
def number_check(n):
    for i in range(2,int(math.sqrt(n))+1):
        if number % i == 0:
            return False
    return True

# 素因数の格納処理
numbers = []
for i in range(2, int(math.sqrt(number))+1):
    if number_check(i):
            while True:
                if number % i == 0:
                    numbers.append(i)
                    number /= i
                else:
                    break
# 入力された値が素数の場合
if not numbers:
    numbers = [number]
print(numbers,end="")


