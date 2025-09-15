def table(inp):
    count=1
    while count<11:
        print(f"{inp} * {count} = {inp*count}")
        count+=1
try:
   table(int(input("Enter number you want to see it table : ")))
except ValueError:
    print("Oops ! , Enter Interger")