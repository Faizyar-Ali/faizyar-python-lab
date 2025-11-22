class user:
    def __init__(self,name,age,password):
        self.name=name #public
        self._age=age #protected
        self.__password=password #private (name_mangling)
user1=user("Mark",17,"jkgdhbcw123")

print(user1.name)
print(user1._age)
print(user1._user__password) 

# These modifiers are just for another developer these make vaibales protected not as cyber secuirity terms instead they ensure someone dont acidentently touch our code means only real programmer who know what he doing can change things in code 