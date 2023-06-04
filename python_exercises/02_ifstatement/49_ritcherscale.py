#richter value 

'''earthquake={
    2.0 : "Micro",
    2.0 < 3.0 :"very minor",
    3.0 < 4.0 :"Minor",
    4.0 < 5.0:"light",
    5.0 < 6.0 :"moderate",
    6.0 < 7.0 :"strong"
    7.0 < 8.0 : "major"
    8.0 < 10.0 " "great"
    10.0 or more :"meteoric"

}'''

earthquake=int(input("enter the value of magnitude:"))
if earthquake > 2.0:
    print("not a earthquake")
elif earthquake == 2.0:
    print("The earthquake is considered to be Micro")
elif earthquake <= 3.0:
    print("The earthquake is to considered to be Very Minor ")
elif earthquake <= 4.0:
    print("The earthquake is considered to be Minor")
elif earthquake <= 5.0:
    print("the earthquake is considered to be light")
elif earthquake <=6.0:
    print("the earthquale is considered to be moderate")
elif earthquake <=7.0:
    print("the earthquake is considered to be strong")
elif earthquake <= 8.0:
    print("the earthquake is considered to be major")
elif earthquake <= 10.0:
    print("the earthquake is considered to be great")
else :
    print("the earthquake is considered to be Meteoric")