def find(ko,filena="test.txt"):
    with open(filena,"r",encoding="utf-8") as file:
       line=1
       while file and line!=5:
          content=file.readline()
          if ko[0:len(ko)] in content:
             return f"{ko} Find on Line {line}"
          line+=1
       return f"{ko} Not Found in your File"
print(find(input("Enter String to find : ")))