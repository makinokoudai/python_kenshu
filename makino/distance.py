
import sys

args = sys.argv

input_place1 = args[1]
input_place2 = args[2]

distance = 0


#辞書の設定
place = {"東京":0.00,"品川":6.78,"新横浜":25.54,"名古屋":342.02 ,"京都":476.31,"新大阪":515.35 }

#場所間の距離の計算と絶対値、小数点の調整
distance =round(abs(place[input_place1] - place[input_place2]),2)  

print(distance,end="")







