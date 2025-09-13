def palin(st):
    res="" 
    lis=[]
    for i in range(len(st)-1,-1,-1):
        if type(st)==str:
           res+=st[i]
        elif type(st)==list:
                 lis.append(st[i])
    if type(st)==str:
         if st.lower()==res.lower():
              return f"The {st} is Palindrome"
         else:
              return f"The {st} isn't Palindrome"
    elif type(st)==list:
         if st==lis:
              return f"The list {st} is Plaindrome"
         else:
              return f"The List {st} is Not Palindrome"
                  
inp=int(input("Choose what you want to see , press 1 or 2 \n1:String \n2:List  =  "))
if inp==1:
    print(palin(input("Enter String you want to seev does it palindrome : ")))
elif inp==2:
     print(palin(list(input("Enter List you want to see does palindrome : "))))   
else:
     print("Enter valid data type")