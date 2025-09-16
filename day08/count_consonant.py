def count_cons(s):
    if len(s) == 0:
        return 0
    first=s[0]
    rest=s[1:]
    if first.isalpha() and first.lower() in "aeiou":
        return count_cons(rest)
    else:
        return 1+count_cons(rest)
user_inp=input("Ebter string to count its consonant : ")
var=count_cons(user_inp)
print(f"{user_inp} contain {var} consonant")
