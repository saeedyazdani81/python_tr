class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The car is driving.")

    def stop(self):
        print("The car has stoped.")

class Truck(Car):
    def __init__(self, make, model, year, color, bed_size, towing_capacity):
        super().__init__(make, model, year, color)
        self.bed_size = bed_size
        self.towing_capacity = towing_capacity
        
class Van(Car):
    def __init__(self, make, model, year, color,passenger_capacity,cargo_space):
        super().__init__(make, model, year, color)
        self.passenger_capacity = passenger_capacity
        self.cargo_space = cargo_space

