# date to holiday name:

day=input('enter the date:')
month=input("enter the name of the month:")

output={
    'January 1':"New year's day",
    'july 1' :"Canada day",
    'December 25': "Christmas day"
    }

holiday = month + " " + day

if holiday in output:
    result = output[holiday]
    print(result)
else:
    print("No matching holiday found.")