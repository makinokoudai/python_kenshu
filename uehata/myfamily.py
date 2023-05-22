import sys
from introfamily import IntroFam

name = sys.argv[1]
age = sys.argv[2]
cat_name = sys.argv[3]

intro = IntroFam(name, age, cat_name)
print(intro.name_out())
print(intro.age_out())
print(intro.cat_name_out())