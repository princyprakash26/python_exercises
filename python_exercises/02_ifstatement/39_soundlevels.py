#sound levels:

'''Jackhammer=130,
Gaslawnmower=106,
Alarm_clock=70,
Quiet_room=40
'''

decibel = int(input("enter the decibel value:"))

if decibel == 130:
    print('Jackhammer')
elif decibel == 106:
    print('Gaslawnmower')
elif decibel == 70:
    print('Alarm_clock')
elif decibel == 40:
    print('Quiet_room')
elif decibel < 40:
    print("enter the valid soundlevels.")
elif decibel < 70:
    print("it is between quiet_room and alarm_clock")
elif decibel < 106:
    print('it is between alarm_clock and gaslawnmower')
elif decibel < 130:
    print('it is between gaslawnower and jackhammer')
else:
    print("There is not morethan 130 decibels at the soundtables")





