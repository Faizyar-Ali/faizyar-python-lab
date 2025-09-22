class Pakistan:
    country="Pakistan"
    def __init__(self,province=None):
        self.province=province

class Nawabshah(Pakistan):
    def __init__(self,city):
        self.city=city
citizen=Nawabshah("Hysdrabad")
print(citizen.city)

class street(Nawabshah):
    def __init__(self,street_no,city):
        super().__init__(city)
        self.street_no=street_no
person=street(23,"Karachi")
print(person.street_no)
print(person.country)
        
    
