def elig(age):
    if age>=18:
        return "Person Can Vote"
    else:
        return "person Can't vote"
age=int(input("Enter Person Age : "))    
print(elig(age))