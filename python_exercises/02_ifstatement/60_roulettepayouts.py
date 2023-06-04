# roulette payouts:

'''wheel spaces=38
18=black
18=red
2=green(0 or 00)
red spaces=1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
remaining(blackspaces)=1-36
'''

import random

result=random.randint(0,36)
redspaces=1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36

if result == 1 or result == 3 or result == 5 or result == 7 or result == 9 or result == 12 or result == 14 or result == 16 or result == 18 or result == 19 or result == 21 or result == 23 or result == 25 or result == 27 or result == 30 or result == 32 or result == 34 or result == 36:
    print(f"The spin resulted in {result}")
    print("Pay",result)
    print('Pay Red')
    print('pay 19 t0 36')
elif result == 0:
    print('pay',result)
elif result != redspaces:
    print("the spin resulted in ",result)
    print('Pay',result)
    print('Pay Black')
    print('Pay 1 to 18')
