class ClassRoom:
    def __init__(self, students):
        self.students = students
    
    def __iter__(self):
        return iter(self.students)

c = ClassRoom(["Ali", "Sara"])
for student in c:
    print(student)
