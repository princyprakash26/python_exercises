#compute the hypotenuse:

import math

def hypotenuse(a,b):
    length_hypo=math.sqrt(a**2 + b**2)
    return length_hypo

def main():
    a=int(input("enter the length:"))
    b=int(input("enter the length"))
    hypolength=hypotenuse(a,b)
    print(hypolength)
main()