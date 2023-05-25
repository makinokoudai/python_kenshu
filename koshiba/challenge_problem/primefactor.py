import sys
args = sys.argv

# 引数を変数に代入
num = int(args[1])

# 空リスト作成
mun_list = []

# 素数検出
for i in range(2, num):
    if num % i == 0:
        mun_list.append(i)
        num = num / i
        while num % i == 0:
            mun_list.append(i)
            num = num / i
        else:
            pass
    else:
        pass

if num == int(args[1]):
    mun_list.append(int(args[1]))

print(mun_list, end="")
