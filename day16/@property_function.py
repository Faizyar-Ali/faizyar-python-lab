class percentage: 
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem
    @property
    def average(self):
          return (self.phy+self.math+self.chem)/3
obj=percentage(10,30,12)    
print(obj.average)
obj.phy=390
print(obj.average)

