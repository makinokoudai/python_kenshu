class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def name_out(self):
        name_txt = "私の名前は、" + self.name + "です"
        return name_txt
    
    def age_out(self):
        age_txt = "年齢は、"+ self.age + "歳です"
        return age_txt
