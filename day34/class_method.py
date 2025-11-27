class Animal:
    sound="I dont have voice"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def sound(cls,s):
        cls.sound=s

cat=Animal("kitty",3)
print(cat.name)
print(cat.age)
cat.sound("Meow")
print(cat.sound)
