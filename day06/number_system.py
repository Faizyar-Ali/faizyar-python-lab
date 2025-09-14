print("============= Number System Converter =============")
try :
    user_input=int(input("Enter a Decimal Number You want to see its Binary Octal Hexadecimal Representation : "))
    bina=bin(user_input)
    octa=oct(user_input)
    hexa=hex(user_input)
    print(f"Binary conversion : {user_input} = {bina}")
    print(f"Octal Conversion  : {user_input} = {octa}")
    print(f"Hexadecimal conversion : {user_input} = {hexa}")
except ValueError:
    print("Oops 😵‍💫 , Only Try To input integer Next time")    

prefix=input("Enter Binary,Octal or Hexadecimal Number to see its Decimal Value  : ")
if prefix.startswith("0b"):
    try : 
       print(f"Decimal conversion : {prefix} = {int(prefix,2)} ")
    except ValueError:
        print("Oops 🫨 , Only 0 and 1 is allowed in Binary system")   
elif prefix.startswith("0o"):
    try:
      print(f"Decimal Conersion from octal to decimal : {prefix} = {int(prefix,8)}")
    except ValueError:
        print("Opps 🫨 '8' or above 8 is invalid in Octal system")
elif prefix.startswith("0x"):

    print(f"Hexadecimal to Decimal conversion : {prefix} = {int(prefix,16)}") 
else:
    print("Conversion failed 😵‍💫 , Try number start with 0b or 0o or 0x")


print("============ Conclusion =============\nWHY THE LEADING ZERO IS NOT ALLOWED IN PYTHON :  \nThe leading zero is not allowed in python because \nin ealry languages like python 2 or C the literal of octal is 0 ,\nbut it causing silent bug and also when the beginner try 0238 they got error du\nto 8 in there input because python treat 0238 as octal and in octal 8 is not allowed so thats why pthon banned it in Python 3 ")

