# free fall:
import math

height = float(input('enter the height:'))
acceleration = 9.8
initial_Speed = 0

final_speed = math.sqrt(initial_Speed**2 + 2 *acceleration*height)

print(final_speed)