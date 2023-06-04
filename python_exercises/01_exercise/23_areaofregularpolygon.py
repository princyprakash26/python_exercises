# area of a regular polygon:
import math

length=int(input('enter the values of length of side:'))
side=int(input('enter the values of number of sides:'))

area = (side *length*length)/ 4 * math.tan(math.pi/side)

print(area)