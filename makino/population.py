
import sys 

args = sys.argv

choose_cty = int(args[1])

countrys = ("China","India","U.S.A","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh","Russia","Mexico")

print(countrys[choose_cty-1],end="")