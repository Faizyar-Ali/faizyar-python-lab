import random
import string
while True:
   values=string.ascii_letters+string.digits+string.punctuation
   while True:
     try: 
      length=int(input("How Much Long You want Password : "))
      break
     except ValueError:
        print("OOps😵‍💫,Enter Lenght in Number ")
   password="".join(random.choice(values) for i in range(length))
   print(f"Generated Password : {password}")
   choice=input("\nNew Password(n)\nExit(any Key)) : ")
   if choice=="n":
       pass
   else:
      break

