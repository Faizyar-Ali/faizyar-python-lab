def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)
print("Your Factorial is = ",factorial(int(input("Enter Number you want to see its Factorial : "))))
