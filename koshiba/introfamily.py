from introduce import Intro

#class Intro:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
    
#    def name_out(self):
#        nametext = "私の名前は、" + self.name + "です"
#        return nametext
    
#    def age_out(self):
#        agetext = "年齢は、" + self.age + "歳です"
#        return agetext


class IntroFam(Intro):    
    def __init__(self, name, age, cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name

    def cat_out(self):
        cattext = "飼い猫の名前は、" + self.cat_name + "です"
        return cattext