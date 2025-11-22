class form:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new):
        if new<18:
            raise ValueError("you Cant Enroll due to Teenager")
        self._age=new
try :
     p1=form("Mark",18)
     print(p1.age)
except ValueError as e:
    print(f"Error : {e}")