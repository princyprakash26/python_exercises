# area of triangle (again)

import math

s1=int(input('enter the value of s1:'))
s2=int(input('enter the values of s2:'))
s3=int(input('enter the values of s3:'))

s=(s1 + s2 + s3)/2

result= math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print(result)