import sys 

num = int(sys.argv[1])

# 素数チェック用関数
def prime_check(n):
    for i in range(2,n//2+1):
        if num % i == 0:
            return False
    return True

# 素因数格納用
prime_factor = []
for j in range(2, num//2+1):
    if prime_check(j):
            while True:
                if num % j == 0:
                    prime_factor.append(j)
                    num /= j
                else:
                    break
# 入力が素数の場合
if not prime_factor:
    prime_factor = [num]
print(prime_factor,end="")