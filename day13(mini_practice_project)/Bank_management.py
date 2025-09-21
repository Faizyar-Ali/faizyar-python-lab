import time
import sys
import os
class Bank:
    def __init__(self,acount_no,name,password,balance):
        self.balance=balance
        self.name=name
        self.__password=password
        self.acount_no=acount_no
    def complete(self):
            va=["\nTransaction Successful ✅\n___________________________________________________\n\n"]
            for i in va:
                if len(i)>1:
                    for o in i:
                        print(o,end="")
                        time.sleep(0.020)
                else:
                    print(i,end="")
    def welcome(self):
         return print("\nHI ",self.name ,"😊  Welcome TO Habib Bank")
    def withdraw(self):
        while True:
            try :
               D_amount=int(input("Enter Amount to Withdraw : "))
               break
            except ValueError:
               print("Oops 😵‍💫 ,Please Enter Amount in Numbers")
               
        self.balance=self.balance-D_amount
    def safepassword(self):
            return self.__password
    def deposit(self):
        while True: 
            try:
                C_amount=int(input("Enter Amount to Deposit : "))
                break
            except ValueError: 
                print("Oosps 😵‍💫,Enter Amount in Numbers : ")        
        self.balance=self.balance+C_amount
        return self.balance
    def pay(self):
       while True: 
        try:
           self.balance=int(input("Enter Amount to pay : "))+self.balance
           self.complete()
           return self.balance
        except ValueError:
            print("Oops 😵‍💫 ,Please Enter Amount in Numbers")
    def loan(self):
                   print(f"\nLoan On You  :{self.balance*-1} \n")
                   print("Please Pay the Loan First to acess Transactions")
                   print("1: Pay Loan ")
                   print("2: Exit(pay Later)")
                   choice=int(input("\nPress Key(1,2) To Go : "))
                   match choice:
                        case 1:
                           self.pay()    
                        case 2:
                            print("\nSee you Again 😉")
                            sys.exit()      
    def access(self):
        self.welcome()
        while True:
            if self.balance>=0:
              print(f"\nYour Current Balance : {self.balance}\n")
              print("1 : Deposit Money")
              print("2 : WithDraw Money")
              print("3: Exit")            
              while True:
                try: 
                  choice=int(input("\nPress Key(1,2,3) To Go : "))
                  if choice in [1,2,3]:
                       break
                  else:
                      print("Oops😵‍💫,Try Key in 1,2,3 ")
                except ValueError:
                    print("Oops 😵‍💫, Try Key in 1,2,3")
              match choice:
                case 1:
                  self.deposit()
                  self.complete()
                case 2:
                  self.withdraw()
                  self.complete()
                case 3:
                    print("\nSee you Again 😉")
                    sys.exit()
            else:
                self.loan()
def clear():
    if os.name=="nt":
        os.system('cls')
    else:
        os.system('clear')   

u1=Bank(1,"Anzal","pass12",8000)
u2=Bank(2,"Taylor","city32",75000)
u3=Bank(3,"SamAltman","sam23",10000)
acounts=[u1,u2,u3]
g=0
while True:
 while g!=10:
    g+=1
    clear()
    A_name=input("Enter Your Acount Name : ")
    password=input("Enter Your Password : ")
    for i in range(len(acounts)):
        if acounts[i].name== A_name and acounts[i].safepassword() == password:
            acounts[i].access()
    else:
            print("Invalid Credentials ❌\n")
            time.sleep(0.4)
 else:
    g=0
    for y in range(10,0,-1):    
            print(f"Please Wait {y} sec",end="\r")
            time.sleep(1)

