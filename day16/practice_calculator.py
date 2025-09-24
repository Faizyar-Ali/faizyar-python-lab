print("Welcome To my Calculator")
cal=int(input("1 : Addition\n2 : Substraction\n3 : Multiplication\n4 : Division : "))
num1=int(input("\nEnter First Number : "))
num2=int(input("Enter Second Number : "))
match cal:
    case 1:
        print(f"{num1} + {num2} is = {num1+num2}")
    case 2:
        print(f"{num1} - {num2} is = {num1-num2}")
    case 3:
        print(f"{num1} * {num2} is = {num1*num2}")
    case 4:
        print(f"{num1} \ {num2} is = {num1/num2}")