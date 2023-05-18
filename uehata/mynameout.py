import sys

# コマンドライン引数の受け取り
# python mynameout.py 引数
args = sys.argv
name = args[1]

# 改行コードなしで出力
print("Hello", name, "!", end="")