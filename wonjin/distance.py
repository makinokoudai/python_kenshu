
eki = {"東京":0,
       "品川":6.78,
       "新横浜":25.54,
       "名古屋":342.02,
       "京都":476.31,
       "新大阪":515.35}

import sys 

start = sys.argv[1]

end = sys.argv[2]

res = 0 

res = eki[end] - eki[start]

print(abs(round(res,2)),end="")

# abs -> 절댓값

