import random

number = []
for integer in range(50):
    integer = random.randint(0,101)
    print(integer)
    number.append(integer)
    maxnum = max(number)

print('maxnum=',maxnum)

