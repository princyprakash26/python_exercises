# admission price:

baby_price = 0.00
child_price = 14.00
senior = 18.00
guest = 23.00

baby = 2
child = 12
adult = 64

total =0

admission = input('enter the age of the guest(blank to quit)')
while admission != '':
    age = int(admission)
    if age <= baby :
        total = total + baby_price
    elif age <= child:
        total = total + child_price
    elif age <= adult :
        total = total + senior
    else:
       total = total + guest
    
    admission = input('enter the age:')

print(f'total for the group is {round(total, 2)}')


