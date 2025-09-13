def multiple(divisor,mult):
    if mult%divisor==0:
        return f"The {mult} is Valid Multiple of {divisor}"
    else:
        return f"The {mult} is InValid Multiple of {divisor}"
mult=int(input("Enter the multiple : ")) 
divisor=int(input("Enter the number to divide by : "))   
print(multiple(divisor,mult))   