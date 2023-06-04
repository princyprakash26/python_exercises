#next day

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))


if (day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10)):
    day = 1
    month += 1
elif (day == 30 and (month == 4 or month == 6 or month == 9 or month == 11)):
    day = 1
    month += 1
elif (day == 31 and month == 12):
    day = 1
    month = 1
    year += 1

elif (day == 28 and month == 2):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        day += 1
    else:
        day = 1
        month += 1
elif (day < 31):     
    day += 1
else:
    print("Invalid date!")

print(f"{day}/{month}/{year}")


