import random
import string
new=""
def encoding(message):
     message=message[1:]+message[0]
     messa=""
     second=""
     if len(message)>=3:
         for i in range(len(message)-1):
             messa+=message[i+1]
         for i in range(3):
              first=random.choice(string.ascii_lowercase)
              message+=first
         for i in range(3):
             second+=random.choice(string.ascii_uppercase)
         message=second+message
         return message
     else:
         new=message[::-1]
         message=new
         return message
def decoding(message):
    if len(message)<3:
        message=message[::-1]
        return message
    else:
          message=message[3:]
          message=message[:-3]
          message=message[len(message)-1]+message[:-1]
          return message
message=input("Type here : ")
print(f"Encoded = {encoding(message)}")
print(f"Decoded = {decoding("PFVellohafn")}")
