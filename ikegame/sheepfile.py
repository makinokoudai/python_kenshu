import sys
arg = int(sys.argv[1])
with open("../../files/sheep.txt","w") as f:
    for i in range(1,arg+1):
        f.write("ひつじが{0}匹\n".format(i))