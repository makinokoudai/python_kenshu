
ls = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")


import sys

country = int(sys.argv[1])

# country = int(input("input"))

print(ls[country-1],end="")
