class Animal:
    def __init__(self,species):
        self.species=species
    def sound(self):
        print("Animals sonud tui tooooo tui tooooooo")
obj=Animal("Bil")
obj.sound()
class Cat(Animal):
    def __init__(self,breed):
        self.breed=breed
    def sound(self):
        print("Miauu")
billi=Cat("Baby Billi")
billi.sound()