import sys
args = sys.argv

# 引数を変数に代入
score_math = int(args[1])
score_japanese = int(args[2])
score_english = int(args[3])

# 合否判定

if 0 <= score_math <= 100 and 0 <= score_japanese <= 100 and 0 <= score_english <= 100:
    # 全科目70点以上または合計点が220点以上か(全科目70点以上の時点で50点未満の科目は1つもない)
    if score_math >= 70 and score_japanese >= 70 and score_english >= 70:
        print('合格', end="")
    elif score_math + score_japanese + score_english >= 220 :
        # 50点未満の科目が1つもなければ合格
        if score_math >= 50 and score_japanese >= 50 and score_english >= 50:
            print('合格', end="")
        else:
            print('不合格', end="")
    else:
        print('不合格', end="")
else:
    print('正しい点数を入力してください')

