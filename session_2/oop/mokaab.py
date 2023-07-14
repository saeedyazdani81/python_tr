from squre import Squre
class Mokaab(Squre):
    def __init__(self, side):
        super().__init__(side)


    def Volume(self):
        return self.area()*6


