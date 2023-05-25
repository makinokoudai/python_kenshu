import func_salary
import sys
args = sys.argv

# 引数を変数に代入
salarys = [int(args[1]), int(args[2]), int(args[3])]

# モジュールの関数を使う

for salary in salarys:
    a, b, c = func_salary.calcsalary(salary)
    print(a, b, c)
    print(type(a))


