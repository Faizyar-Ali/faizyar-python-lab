
from datetime import datetime
import sys
now=datetime.now()  
current_time=now.strftime("%S") 
print("""---------------------------Check Your Typing Speed---------------------------\n\nZuckerberg's early career, legal troubles and initial success with Facebook, The Social Network, was released in 2010 and won multiple Academy Awards. His prominence and fast rise in the technology industry has prompted political and legal attention. He has been the subject of multiple lawsuits regarding the creation and ownership of the website as well as issues such as user privacy.""")
choice=input("\n\nStart Typing above paragranph(p)\nQuit(q) : ")
if choice.lower()=="p":
    print("Your Time has Started...")
    start=datetime.now()
    typing=input(" : ")
    end=datetime.now()
    duration=(end-start).total_seconds()
    print(f"You Complete Task in {duration:.2f} second")
elif choice.lower()=="q":
    print("Good Bye")
    sys.exit()
else:
    print("Choose Valid Choice")
duration=int()-int(current_time)