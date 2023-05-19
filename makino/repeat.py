
import sys

args = sys.argv

input_number = int(args[1])

count = 0

while count <= 100:
    count += input_number
    
    if count==100 :
        print("Just 100!",end="")
        break
    elif count > 100:
        print("Over!",end="")
        
  