
# import sys 

# n = int(sys.argv[1])

# for i in range (n):
#     print(f"ひつじが{i+1}匹")

## 리스트 조작 

# ls = ["giraffe","tigger","zebra","elephant","lion"]

# ls.append("rabbit") # 리스트의 마지막 요소에 추가 

# ls.insert(2,"pig") # insert ( 입력할 값, 인덱스 )

# print(ls)

# m = [2,5,7]

# n = [3,5,9]

# k=m+n
# # print(k) # 리스트의 더하기 

# k += [11,13]

# print(k)

# 리스트를 추가하는 함수는 extend 

# k.extend([15,17,19]) 

# # print(k)

# # 리스트의 원소를 삭제 

# # remove ( 찾을 값 )

# k.remove(3)

# print(k)

# 리스트에서는 a[1] = 555 하면, 인덱스 1번의 값이 갱신 

# a.insert(1,555) -> 인덱스 1번에 555가 추가 

# remov 는 삭제할 값을 검색하여, 삭제를 하고, 

# del는 삭제하고 싶은 인덱스를 찾아서 삭제한다. 



# import random 

# a=["1","2","3","4"]

# i=random.randint(0,len(a)-1)

# print(i)

# n = [1,2,3]

# n.append([5,6,7,8,9,10])

# print(n)

# 슬라이스 

# 리스트 [ 개시 : 완료 ]
# a=[1,2,3,4,5]
# print(a[1 : 3])

# b = [0,1,2,3,4,5,6,7]

# print(b[1:3])

# print(b[2:]) 

# num = [0,1,2,3,4]

# del num[4]

# print(num)

# # pop 은 마지막 요소를 출력하고, 삭제한다. 

# pop(num[3])



