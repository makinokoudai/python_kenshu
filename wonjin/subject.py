import sys
a=[]
res=0
# n = map(int,sys.argv[1:])


n = list(map(int,sys.argv[1:]))



for i in range(len(n)): 
   
    
    if n[i] >= 70 :
        res = res + n[i]


if res >= 220:
    print("合格",end="")