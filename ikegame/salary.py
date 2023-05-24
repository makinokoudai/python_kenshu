from decimal import Decimal,ROUND_HALF_UP

#間違えそうなので定数にしておく
BOUND = 1000000

def calc_salary(pay):

    #額面給与を100万より上と以下にわける
    #100万より上の部分がマイナスの場合は額面が100万以下であるので、上の部分は0に直す
    upper_pay = pay - BOUND
    if upper_pay < 0:
        upper_pay = 0

    #以下の部分
    lower_pay = pay - upper_pay

    #それぞれの税額計算
    lower_tax = lower_pay * 0.1
    upper_tax = upper_pay * 0.2

    #税額をがっさんして四捨五入
    tax = lower_tax + upper_tax
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

    #支払い額は額面-税額
    payment = pay - tax
    return payment