import sys

args =  sys.argv

number =int(args[1]) 

if number % 2 == 0 :
    print("偶数",end="")
else:
    print("奇数",end="")