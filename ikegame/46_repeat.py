import sys
i = 0
arg = int(sys.argv[1])
while True:
    if i == 100:
        print("Just 100!",end="")
        break
    elif i > 100:
        print("Over!",end="")
        break
    i += arg