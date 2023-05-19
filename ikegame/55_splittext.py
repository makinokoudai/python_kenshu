import sys
sent, n = sys.argv[1:3]

print(sent.split(" ")[int(n) - 1])