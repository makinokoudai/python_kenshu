import sys
n_in = int(sys.argv[1])

res = []
n = 2
while n <= n_in:
    if n_in % n == 0:
        res.append(n)
        n_in = int(n_in / n)

    else:
        n += 1

print(res,end="")