class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def name_out(self):
        nametext = "私の名前は、" + self.name + "です"
        return nametext
    
    def age_out(self):
        agetext = "年齢は、" + self.age + "歳です"
        return agetext
    