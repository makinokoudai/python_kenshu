import sys

args = sys.argv

input_name = args[1]
input_downprice = int(args[2])


hinmoku = {'果物類':{'リンゴ':80, 'みかん':198,'バナナ':150}, '酒類名':{'ビール':360, '日本酒':580,},'麺類':{'ラーメン':280,'うどん':28,'パスタ':158}}

if input_name == "果物類" :
    for i in hinmoku[input_name]:
        hinmoku[input_name][i] -= input_downprice
        if hinmoku[input_name][i] < 0 :hinmoku[input_name][i] = 1
        
        
if input_name == "酒類名" :
    for i in hinmoku[input_name]:
        hinmoku[input_name][i] -= input_downprice
        if hinmoku[input_name][i] < 0 :hinmoku[input_name][i] = 1

if input_name == "麺類" :
    for i in hinmoku[input_name]:
        hinmoku[input_name][i] -= input_downprice
        if hinmoku[input_name][i] < 0 :hinmoku[input_name][i] = 1
        


hinmoku = hinmoku['果物類']|hinmoku['酒類名']|hinmoku['麺類']


print(hinmoku)