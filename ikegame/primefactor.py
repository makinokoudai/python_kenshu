import sys
import copy
n_in = int(sys.argv[1])

res = []
n = 2

tmp = n_in
limit = copy.deepcopy(n_in)
while n <= limit:
    if tmp % n == 0:
        res.append(n)
        tmp = int(tmp / n)
        limit = int(n_in / n)
    else:
        n += 1


print(res,end="")