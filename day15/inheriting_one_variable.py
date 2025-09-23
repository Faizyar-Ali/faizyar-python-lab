class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,salary=None):
        super().__init__(name,salary)
obj=Manager("Basit")
print(obj.name)