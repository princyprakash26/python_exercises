# Days in month


import calendar

def get_days_in_month(month, year):
    if month < 1 or month > 12:
        return -1

    if year < 1000 or year > 9999:
        return -1

    days = calendar.monthrange(year, month)[1]
    return days


def main():
    month = int(input("Enter the month in numbers: "))
    year = int(input("Enter the year: "))

    num_days = get_days_in_month(month, year)

    if num_days == -1:
        print("Invalid month or year.")
    else:
        print(f"Number of days in month {month}, year {year}: {num_days}")


main()
