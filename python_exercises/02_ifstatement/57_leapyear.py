# Is it a leap year

year=int(input("enter the year to check it is leap or not:"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It is a leap year")
else :
    print("It is not a leap year")