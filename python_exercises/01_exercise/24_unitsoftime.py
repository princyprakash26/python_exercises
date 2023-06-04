# units of time:

days = int(input('enter days:'))
hours = int(input('enter the hours:'))
minutes = int(input('enter the minutes:'))
seconds = int(input('enter the seconds:'))

total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60)+(minutes * 60)+ seconds

print(total_seconds)