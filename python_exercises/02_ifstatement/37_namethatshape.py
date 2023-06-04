#Name that shape:

shape = int(input("enter the sides of the shapes:"))

if shape <= 2:
    print("Enter a appropriate sides")
elif shape == 3:
    print("The Triangle has 3 sides")
elif shape == 4:
    print("The Square has 4 sides")
elif shape == 5:
    print("The pentagon has 5 sides")
elif shape == 6:
    print("The hexagon has 6 sides")
elif shape == 7:
    print("The heptagon has 7 sides")
elif shape == 8:
    print("The octagon has 8 sides")
elif shape == 9:
    print("The nonagonn has 9 sides")
elif shape == 10:
    print("The decagon has 10 sides")
else:
    print("there is no sides morethan 10,enter the appropriate value: ")
