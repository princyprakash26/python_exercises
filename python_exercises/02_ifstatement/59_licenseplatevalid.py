#Is a license plate valid

'''
older_plate= AAA 112
newer_plate= AAA 1111
'''

plate = input("enter the character of licence late:")

if len(plate) == 7 and plate[3] == " " and int(plate[4]) and int(plate[5]) and int(plate[6]):
    print("this is valid for old plate license")
elif len(plate) == 8  and plate[3] ==" " and int(plate[4]) and int(plate[5]) and int(plate[6]) and int(plate[7]):
    print("This is valid for new plate license")
else:
    print("This is not valid for a license plate")

