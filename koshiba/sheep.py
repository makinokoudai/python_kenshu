import sys
args = sys.argv

# 引数を変数に代入
sheep_setting = int(args[1])

# ひつじのループ
for i in range(1, sheep_setting+1):
    print(f'ひつじが{i}匹')
