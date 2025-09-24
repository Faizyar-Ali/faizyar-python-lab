class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return 22/7*(self.radius**2)
    def perameter(self):
        return 2*(22/7)*self.radius
circl=Circle(10)
print(circl.Area())
print(circl.perameter())