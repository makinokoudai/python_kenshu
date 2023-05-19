import sys 

i = int(sys.argv[1])
res=0
while True:

    if res == 100:
        print("Just 100!",end="")
        break
    elif res > 100: 
        print("Over!",end="")
        break
    res+=i
