import sys
args = sys.argv

# 引数を変数に代入
text_english = args[1]
text_number = int(args[2])

# 文字列を分割
text_english.split()

# n番目の単語を出力
print(text_english.split()[text_number-1], end="")