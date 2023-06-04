# is prime nummbers:

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def main():
    n = int(input("Enter a number: "))
    result = is_prime(n)
    
    if result:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")



main()
