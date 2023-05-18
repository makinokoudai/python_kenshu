import sys
# コマンドライン引数で給与額を受け取る
salary = int(sys.argv[1])

# 税額と支給額の初期化
after_tax = 0 
tax = 0

# 税率
tax_rate = [0.1,0.2]

# 税金計算基準額
BASE = 1000000

# 給与が100万を超えている時の処理
if salary > BASE:
    # 100万を超えた分
    exceed = salary - BASE
    # 100万を超えた額に対して20%の税率
    tax += exceed * tax_rate[1]
    # 100万に対して10%の税率
    tax += BASE * tax_rate[0]
else:
    # 給与額に対して10%の税率
    tax += salary * tax_rate[0]

# 支給額の算出
after_tax = salary - tax

# 少数第一位を四捨五入
tax = round(tax)
after_tax = round(after_tax)
print(f"支給額:{after_tax}、税額:{tax}",end="")
    
