def Grade(per):
    if per>=60 and per<70:
      return 'You Got "C" Grade'
    elif per>=70 and per<80:
      return 'You Got "B" Grade'
    elif per>80 and per<90:
        return 'You Got "A" Grade'
    elif per>90 and per<100:
        return 'Hurahhh You "A+" Grade '
    else:
        return "You FAILED  , You Need More Iprovement "
per=int(input("Enter Your Percentage :"))
print(Grade(per))