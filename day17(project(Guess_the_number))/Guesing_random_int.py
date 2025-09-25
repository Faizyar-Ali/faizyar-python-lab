import random
secret_num=random.randint(1,10)
def num(secret_num):
   print(f"\nThe Number was {secret_num}")
while True: 
   try:
    choice=input("\nGuess the Number\nQuit the Game(q)  : ")
    if choice=="q":
       num(secret_num)
       break
    else:
       choice=int(choice)
    if choice==secret_num:
        print(f"You Win\nyour choice = {choice} Number = {secret_num}")
        ask=input("\nPlay Again(p)\nLeave the game(e)")
        if ask=="e":
           break
        else:
           secret_num=random.randint(1,10)
    elif choice in [secret_num-2 , secret_num-1,secret_num+2 , secret_num+1]:
        print("You are Very close!\nTry Again")
    else:
        print("you are too far from number")
   except ValueError:
     print("\nEnter the Number,\nCharacter are not allowed")
print("------------------------ GAME OVER --------------------------")

