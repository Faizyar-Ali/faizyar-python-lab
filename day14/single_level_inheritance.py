class car:
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")
class Honda(car):
    def __init__(self,name):
        self.name=name
obj=Honda("Civic")
print(obj.name)
obj.start()
obj.stop()