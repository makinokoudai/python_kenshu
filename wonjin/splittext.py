import sys 
word = sys.argv[1]
num = int(sys.argv[2])
a = word.split()
print(a[num-1],end="")