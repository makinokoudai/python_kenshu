distance = {
    "東京":0.00,
    "品川":6.78,
    "新横浜":25.54,
    "名古屋":342.02,
    "京都":476.31,
    "新大阪":515.35
}
import sys
dep,dest = sys.argv[1:3]
from fractions import Fraction
print(abs(float(Fraction(str(distance[dest])) - Fraction(str(distance[dep])))),end="")