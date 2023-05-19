import sys
i,anim = sys.argv[1:3]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(int(i),anim)

animals.pop(-1)
animals.sort()

print(animals,end="")