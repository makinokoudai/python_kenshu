import sys
import func_salary

salary_list = sys.argv[1:]
for salary in salary_list:
    after_tax, tax = func_salary.calcsalary(int(salary))
    print(f"給与: {salary}、支給額: {after_tax}、税額: {tax}")