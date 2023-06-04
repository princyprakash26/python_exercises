# is it a valid triangle

def valid_triangle(a1,b2,c3):
    if a1 > b2+c3 :
        return False
    else :
        return True

def main():
    a1=int(input("enter the triangle length 1:"))
    b2=int(input("enter the length for triangle 2:"))
    c3=int(input('enter the length for the triangle 3:'))
    result=valid_triangle(a1,b2,c3)
    print(result)
main()
