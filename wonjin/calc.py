
import sys 



z=0
for i in sys.argv[1:]:
    z=int(i)+z
print(int(z),end="")