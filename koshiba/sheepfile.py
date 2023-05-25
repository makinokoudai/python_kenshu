import sys
args = sys.argv

# ファイルの読み書き
sh = open("../../files/sheep.txt", mode="w", encoding="utf-8")
for i in range(1, int(args[1])+1):
    if i < int(args[1]):
        sh.write(f'ひつじが{i}匹\n')
    else:
        sh.write(f'ひつじが{i}匹')

sh.close