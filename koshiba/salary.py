from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv

# 引数を変数に代入
salary = int(args[1])

# salary = Decimal(str(salary)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

#給与で税率変更
if salary > 1000000:
    tax = (salary - 1000000) * 0.2 + 1000000 * 0.1
else:
    tax = salary * 0.1

# 税率から支給額算出
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
amount = salary - tax

# 結果を出力
print(f'支給額:{amount}、税額:{tax}', end="")