class Students:
    def __init__(self,name,Marks):
        self.name=name
        self.Marks=Marks
    def average(self):
        num=0
        for i in self.Marks:
            num+=i
        return num/len(self.Marks)
s1=Students("Rafay",[81.5,79,80])
print(f"Hi {s1.name} your avegrage marks are {s1.average()}")

s2=Students("Basit",[87,75,90])
print(f"Hi {s2.name} your avegrage marks are {s2.average()}")