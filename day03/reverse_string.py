def river(na):
    if len(na)==0:
        return na
    var = river(na[1: ])
    return var+na[0]
print(river("faizyar"))