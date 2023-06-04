#greatest common divisor:


n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

d = min(m, n)
print(d)

while m % d != 0 or n % d != 0:
    d -= 1

print(d)


