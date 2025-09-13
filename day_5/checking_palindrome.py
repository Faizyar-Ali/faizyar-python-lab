def palin(word):
    f=""
    for i in word[::-1]:
        f+=i
    if f.lower()==word.lower():
        return "The String is Palindrome"
    else:
        return "The String isn't Palindrome"
print(palin(input("Enter word to check palidrmoicity : ")))

     