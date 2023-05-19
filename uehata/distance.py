import sys 

# 新幹線の停車駅と東京駅からの距離を辞書に格納
distance_dict = {
    "東京" : 0.00,
    "品川" : 6.78,
    "新横浜" : 25.54,
    "名古屋" : 342.02,
    "京都" : 476.31,
    "新大阪" : 515.35
}

# 1つ目の駅
start_pt = sys.argv[1]
# 2つ目の駅
end_pt = sys.argv[2]

# 駅名リスト
stations = list(distance_dict.keys())

# ======= +a 例外処理 ========

# distance_dictに登録されていない駅名が入力されたとき
if (start_pt not in stations) or (end_pt not in stations):
    
    # 新幹線の停車駅を一覧表示する
    print("※ 以下の駅名から選択してください。")
    for station in stations : print(f" ・ {station}")
    # プログラムを終了する
    sys.exit()

# ======= +a 例外処理 ========

# 始点から終点から間での差分を取り, 少数第2位までの絶対値を求める
distance = abs(round(distance_dict[end_pt] - distance_dict[start_pt],2))

# 2つの駅間の距離を出力する
print(distance,end="")