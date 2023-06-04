#wave length:

colour=int(input("enter the wavelength:"))

if 380 <= colour <=450:
    print("violet")
elif 450 <= colour <= 495:
    print("Blue")
elif 495 <= colour <= 570:
    print("Green")
elif 570 <= colour <= 590:
    print("Yellow")
elif 590 <= colour <= 620:
    print("Orange")
elif 620 <= colour <=750:
    print("Red")
else:
    print("it is outside of the visible spectrum")