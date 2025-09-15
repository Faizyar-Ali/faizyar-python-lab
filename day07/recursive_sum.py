def natural(n):
    if n==1:
        return 1
    return n+natural(n-1)
print(natural(int(input("Enter number till you want to sum natural number : "))))

