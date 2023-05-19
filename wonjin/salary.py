from decimal import Decimal, ROUND_HALF_UP


## 세률은 100만엔을 넘는 부분은 20 % , 100만엔 이하의 부분에 

# 대해서는 10%이다. 

# 계산식 -> 급여 - 세금 = 지급액, 급여 * 세률 = 세금 액 

# salary = int(input("input your salary ( 万円 ) : " ))
import sys

salary =int(sys.argv[1])

if salary > 1000000:
    res = salary - 1000000 
    zekin = res * 0.2 + (1000000*0.1)
    salary_real = salary -  zekin
else : 
    zekin = salary * 0.1
    salary_real = salary - zekin

print(f"支給額: {round(salary_real)}、税額: {round(zekin)}",end="")

import sys

# n = int(input('입력 : '))
# sum = 0
# for i in range(n):
#     a = int(sys.stdin.readline())
#     sum += a
# print(sum)
