with open("Practice.txt","r") as a:
    content=a.read()
    new=content.replace("Hello","java")
    print(new)
with open("Practice.txt","w") as we:
    we.write(new)
with open("Practice.txt","r") as n:
    o=n.read()
if "java" in o:
        print(a,"found")
print("Not I. Found")