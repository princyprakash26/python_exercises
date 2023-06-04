# prime factors:

n = int(input("enter the value of n:"))

factor = 2
while factor <= n:
    if n%factor == 0:
        print(factor)
        n = n//factor
    else:
        factor += 1


