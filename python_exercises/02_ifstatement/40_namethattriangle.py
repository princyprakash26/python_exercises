# Name hat triangle:

triangle_side1 = (input("enter the whether it is same or different: "))
triangle_side2 = (input("enter the whether it is same or different: "))
triangle_side3 = (input("enter the whether it is same or different: "))

if triangle_side1 == 'same' and triangle_side2 == 'same' and triangle_side3 == 'same':
    print("It is Equilateral triangle")
elif triangle_side2 == 'same' and triangle_side2 =='same' and triangle_side3 == 'different':
    print("It is isosceles triangle")
elif triangle_side3 =='different' and triangle_side1 == 'different' and triangle_side2 == 'different':
    print("It is a scalene triangle")
else:
    print("Error:enter the required input")