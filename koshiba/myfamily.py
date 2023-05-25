# インスタンスのインポート
import introfamily

# intro = introduce.Intro(name="koshiba", age="24")
intro_fam = introfamily.IntroFam(name="koshiba", age="24", cat_name="dog")

# 出力
print(intro_fam.name_out())
print(intro_fam.age_out())
print(intro_fam.cat_out())
