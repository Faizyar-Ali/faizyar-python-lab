class Students:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    @classmethod
    def from_string(cls,var):
        name,age,mark=var.split("-")
        return cls(name,int(age),mark)

var="faizyar-34-490"
s1=Students.from_string(var)    
print(s1.name)
print(s1.age)
print(s1.mark)
print(help(Students))
#we use class method as alternative constructure becasue if in company or anywhere we data is coming in diffrent forms(Faizyar-13 or faizyar 12 or faizyar_34)