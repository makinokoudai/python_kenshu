
import sys
ls = [  "giraffe", "tiger", "zebra", "elephant", "lion"]  

i=int(sys.argv[1])
z = sys.argv[2]
#1.

ls.insert(i,z)
#2. 
ls.pop()

#3.
ls.sort()

print(ls,end="")
