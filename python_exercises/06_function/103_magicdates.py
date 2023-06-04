# magic dates:

def is_magic_date(date):

    day, month, year = date.split('/')
    day=int(day)
    month=int(month)
    year= int(year) %100
    
    magic= month * 10==year
    return magic
    
date = input("Enter a date (dd/mm/yyyy): ")
if is_magic_date(date):
    print("Magic date!")
else:
    print("Not a magic date.")




