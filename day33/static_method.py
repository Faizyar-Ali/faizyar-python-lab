class random:
    def __init__(self,num):
        self.num=num
    def sum(self,n):
        print(self.num+n)
    
    @staticmethod
    def substract(a,b):
        print(a-b)
n=random(3)
n.sum(9)
n.substract(4,6)

#we can make this method outiside of class but if we want that when we share our class then this method also go with it then we use @staticmethod to store a method without self parameter in class 