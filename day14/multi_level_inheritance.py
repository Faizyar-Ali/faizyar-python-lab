class college:
    college_name="Quest"
    @staticmethod
    def code():
        print("Your COllege ID is 26730")
class Department(college):
    @staticmethod
    def Deggre_in():
        print("Your Degree is in BS")
class Computerscience(Department):
    f="fcadad"
    def __init__(self,name):
        self.name=name
obj=Computerscience("Fahad")
print(obj.name)
print(obj.college_name)
obj.Deggre_in()
    