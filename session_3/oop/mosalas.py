from rectangle import Rectangle
class Mosalas(Rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return self.height * self.width / 2
    
