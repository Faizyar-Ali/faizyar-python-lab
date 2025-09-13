def odev(num):
    if num%2==0:
        return "The number You Enter is EVEN"
    if num%2==1:
        return "The number you enter is ODD"
    else:
        return "Enter Valod Number"
try:
    print(odev(int(input("Enter You want to check odd or even : "))))
except ValueError:
    print("Invalid Integer Let Try 0-9")    