import sys

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

index = int(sys.argv[1])
animal_name = sys.argv[2]


# 第1引数で指定したindexに第2引数で指定した動物名を挿入する
animals.insert(index, animal_name)

# リストの最後の要素を取り出す
animals.pop()

# 昇順ソート
animals.sort()

print(animals,end="")
