#coin flip stimulation:

import random

for i in range(3):  
    flips = []                             #initialize empty list:
    for i in range(3):
        flip = random.choice('H''T')     #random.choice()
        flips.append(flip)

    result = ''.join(flips)        #join
    print(result)                   


