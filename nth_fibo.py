def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(int(input("enter the fibonacci term:\n")) - 1))

#Python
