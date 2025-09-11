def fibonaci(n):
    sequence=[]
    a,b=0,1
    for i in range(n):
        sequence.append(a)
        a,b=b,a+b
    return sequence
print(fibonaci(10))        