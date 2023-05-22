import sys
args = sys.argv

#関数を定義
def calcvalue(*args):
    '''
    可変長引数を使用する場合
    '''
    for num in args:
        #あまりを算出
        mod = num % 2

        #あまりの値から奇数偶数判定
        if mod != 0:
            print(str(num) + "は奇数")
        else:
            print(str(num) + "は偶数")

if __name__ == "__main__":
    import sys
    nums = list(map(int,sys.argv[1:]))
    # numsリストをアンパックして渡す
    calcvalue(*nums)