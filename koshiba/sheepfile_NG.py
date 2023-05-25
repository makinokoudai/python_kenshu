import sys
args = sys.argv

# ファイルの読み書き
sh = open("../../files/sheep_NG.txt", mode="a", encoding="utf-8")
for i in range(1, int(args[1])+1):
        sh.write(f'ひつじが{i}匹\n')

sh.close