import time 
def name(name):
  def greet(fx):    
    def nest(*args,**kwargs):
        print(f"HellO {name}")
        return fx(*args,**kwargs)
    return nest
  return greet

@name("zoaib")
def do():
    print("let Go")
@name("zoiab")
def de(a,b,**kwargs):
    print(a-b,kwargs)
do()
de(3,4,name="Faizyar")