import sys

# 0 オリジンであるため、入力値から1引く
rank = int(sys.argv[1]) - 1

countries = (
    "China",
    "India",
    "U.S.A",
    "Indonesia",
    "Pakistan",
    "Brazil",
    "Nigeria",
    "Bangladesh",
    "Russia",
    "Mexico"
)

print(countries[rank],end="")



