#enter the name of month of days and display the number of days

month_name = input("Enter the month name:").lower()

if month_name =='january' or month_name == 'march' or month_name == 'may' or month_name == 'july' or month_name == 'august' or month_name == 'october' or month_name == 'december' or month_name == 'september':
    print(f"This month {month_name} has 31 days")
elif month_name == 'february':
    print(f"This month {month_name} has 28 days and 29 days if it is a leap year.")
else:
    print(f"This month {month_name} has 30 days.")