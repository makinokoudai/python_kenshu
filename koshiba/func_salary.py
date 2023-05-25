from decimal import Decimal, ROUND_HALF_UP

# 「給与」を渡すおよび「支給額」と「税額」を戻り値として戻す関数
def calcsalary(salary):
        #給与で税率変更
        if salary > 1000000:
            tax = (salary - 1000000) * 0.2 + 1000000 * 0.1
        else:
            tax = salary * 0.1

        # 税率から支給額算出
        tax = int(Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP))
        amount = salary - tax

        # 結果を出力
        return salary, tax, amount
