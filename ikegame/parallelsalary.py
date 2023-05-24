from salary import calc_salary

pays = [100000000,300000000,111]
for pay in pays:
    payment = calc_salary(pay)
    print("支給額:" + str(payment) + "、税額:" + str(pay - payment))
    