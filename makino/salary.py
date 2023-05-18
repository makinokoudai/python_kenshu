from decimal import Decimal , ROUND_HALF_UP

import sys

args = sys.argv

from decimal import Decimal,ROUND_UP

total_salary = int(args[1])
salary = 0


if total_salary >= 1000000 :
    # 20%の処理
    salary_pulled_100 = total_salary - 1000000 
    taxed_20 = salary_pulled_100 * 0.2
    taxed_10 = 1000000 * 0.1
    
    tax = Decimal(taxed_10+taxed_20).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    
    salary = total_salary - (tax)
    
    print(f"支給額:{salary}、税額:{tax}",end="")
else :
    # 10%の処理
    salary = total_salary - (total_salary * 0.1)
    print(f"支給額:{int(salary)}、税額:{int(total_salary*0.1)}",end="")