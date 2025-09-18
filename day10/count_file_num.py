with open("test2.txt","r") as f:
    data=f.read()
    nums=data.split(",")
    eve=0
    od=0
    for i in nums:
        if int(i)%2==0:
          eve+=1
        else:
           od+=1
    print(f"In Your File \neven number = {eve} \nOdd numbers = {od}")