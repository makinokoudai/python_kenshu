import sys
a=[]
res=0
for i in sys.argv[1:]: 
    
    if i >= 70 :
        res = int(res) + int(i)
      

if int(res) >= 220:
    print("合格",end="")