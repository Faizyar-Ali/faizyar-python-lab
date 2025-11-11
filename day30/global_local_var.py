a=5
print(a)
def hello():
    global a
    a=6
    print(a)
hello()
print(a)