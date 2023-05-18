import sys
scores = sys.argv[1:]
# スコア配列をstr -> int に型変換して分割代入
mt_score, ja_score, en_score = map(int, scores)

# 合格の3条件
rule1 = mt_score >= 70 & ja_score >= 70 & en_score >= 70
rule2 = mt_score + ja_score + en_score >= 220
rule3 = mt_score >= 50 & ja_score >= 50 & en_score >= 50


if rule1 or rule2:
    if rule3:
        print("合格",end="")
    else:
        print("不合格",end="")
else:
    print("不合格",end="")