class Country:
    continent = "Asia"
    def __init__(self,name):
        self.name=name
class City(Country):
    def __init__(self,population,name):
        super().__init__(name)
        self.population=population
cont_name=City(None,"Karachi")
print(cont_name.name)
print(cont_name.continent)