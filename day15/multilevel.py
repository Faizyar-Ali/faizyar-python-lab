class Vehicle:
    def __init__(self,maxspeed):
        self.maxspeed=maxspeed
class Car(Vehicle):
    def __init__(self,seats,maxspeed):
        super().__init__(maxspeed)
        self.seats=seats
class ElectricCar(Car):
    def __init__(self,battery_capacity,seats,maxspeed):
        super().__init__(seats,maxspeed)
        self.battery_capacity=battery_capacity
cycle=ElectricCar("1000mph ",4," 5000")
print(cycle.battery_capacity,cycle.seats,cycle.maxspeed)