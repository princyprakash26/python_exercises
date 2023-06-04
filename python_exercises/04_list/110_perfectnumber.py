# perfect number:

def perfect_number(n):
    divisors = []
    for i in range(1,n//2+1):
        if n % i == 0:
            divisors.append(i)
          

    return sum(divisors)         # sum the list

def main():
 
    for x in range(1,10001):
        if perfect_number(x)== x:
            print(x)
main()    