import sys
arg = sys.argv[1]

if int(arg) % 2 == 1:
    print("奇数",end="")
else:
    print("偶数",end="")