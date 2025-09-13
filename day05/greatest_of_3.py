def great(n1,n2,n3):
    if n1>n2 and n1>n3:
        return "Number 1 is Greatest in All"
    elif n2>n3:
        return "Number 2 is Greatest in ALL"
    elif n3>n2:
        return "Number 3 Is "
    else:
        return "All are Equal"
n1=int(input("Enter Number 1 : "))
n2=int(input("Enter Number 2 : "))
n3=int(input("Enter Number 3 : "))
print(great(n1,n2,n3))
