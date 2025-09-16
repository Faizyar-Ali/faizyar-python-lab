def sum_mix(ls):
    if len(ls) ==0:
        return 0
    first=ls[0]
    rest=ls[1:]
    if type(first)==int:
        return first+sum_mix(rest)
    else:
        return sum_mix(rest)
print(sum_mix([1,"hellow",34,65,"world"]))