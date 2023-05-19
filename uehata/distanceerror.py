import sys 

distance_dict = {
    "東京" : 0.00,
    "品川" : 6.78,
    "新横浜" : 25.54,
    "名古屋" : 342.02,
    "京都" : 476.31,
    "新大阪" : 515.35
}

start_pt = sys.argv[1]
end_pt = sys.argv[2]
try : 
    # 始点から終点から間での差分を取り, 少数第2位までの絶対値を求める
    distance = abs(round(distance_dict[end_pt] - distance_dict[start_pt],2))
    print(distance,end="")
except:
    print("のぞみの停車駅を引数に設定してください")
    