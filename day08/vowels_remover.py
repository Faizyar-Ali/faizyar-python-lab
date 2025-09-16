def vow(wor):
    if len(wor)==0:
           return ""
    first=wor[0]    
    rest=wor[1:]
    if first in "aeiou":
          return vow(rest)
    else:
       return first+vow(rest)
print(vow(input("Enter String to remove its vowels : ")))