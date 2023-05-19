import sys

args = sys.argv

input_eng = str(args[1])
input_number = int(args[2])


spl_str = input_eng.split()

print(spl_str[input_number - 1],end="")
