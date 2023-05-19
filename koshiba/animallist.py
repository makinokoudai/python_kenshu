import sys
args = sys.argv

# 引数を変数に代入
number = int(args[1])
new_animal = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(number,new_animal)
animals.pop()
animals.sort()
print(animals, end="")