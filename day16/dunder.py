class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"your Name {self.name}\nYour Age : {self.age}"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Student({self.name!r}, {self.age!r})"
    def __len__(self):
        return len(self.name)
stu=Student(["Faizy","Faizyar","Ali"],19)
print(stu)
print(len(stu))
stu2=Student("Faizy",19)
print(stu2)