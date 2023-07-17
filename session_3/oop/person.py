class Person:
    def __init__(self, name ,family) -> None:
        self.name = name  #property
        self.family = family

    #method
    def introduce_yourself(self):
        return "hello, my name is" , self.name , self.family














person_1 = Person("Hamid" , "Safari")

person_1.introduce_yourself()