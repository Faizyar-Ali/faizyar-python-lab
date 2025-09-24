class Employee:
    def __init__(self,role,department,salray):
        self.role=role
        self.department=department
        self.salary=salray
    def showDetail(self):
        print(f"Your Salary = {self.salary}")
        print(f"Your department is {self.department}")
        print(f"Your role = {self.salary}")
class Engineer(Employee):
        def __init__(self,name,age,role,department,salary):
             super().__init__(role,department,salary)
             self.name=name
             self.age=age
worker=Engineer("Rafay",22,"Python Developer","Computer Science",50000)
print(f"Name : {worker.name}\nAge : {worker.age}\nRole : {worker.department}\nSalary : {worker.salary}\n\n")
worker.showDetail()