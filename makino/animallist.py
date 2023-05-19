import sys 

args = sys.argv

# リストに差し込む場所を指定
insert_number = int(args[1])

# リストに差し込む動物の名前を指定
animal_name = args[2]

animal_arr = ["giraffe","tiger","zebra","elephant","lion"]

animal_arr.insert(insert_number,animal_name)


# リストの最後の要素を取り出す
animal_arr.pop()

# 昇順ソート
animal_arr.sort()

print(animal_arr,end="")

