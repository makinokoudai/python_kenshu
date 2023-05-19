import sys

argus = sys.argv

input_number = int(argus[1]) 
sum = 0

for i in range(1,input_number+1):
    sum += i
    print(f"ひつじが{i}匹")
    