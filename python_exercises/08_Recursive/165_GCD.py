#Greatest common divisor:

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)
    
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
solution = euclid(a,b)
print(solution)