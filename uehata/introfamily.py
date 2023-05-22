from introduce import Intro

class IntroFam(Intro):
    def __init__(self,name, age, cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name
    
    def cat_name_out(self):
        cat_txt = "飼い猫の名前は、" + self.cat_name + "です"
        return cat_txt
