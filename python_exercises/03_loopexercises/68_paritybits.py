#parity bits:

data = input('enter the 8bits:')


if  len(data) != 8 :
    print('enter 8 bits (0 or 1)')

else:
    ones = data.count('0')

if ones % 2 ==0:
    print('the bit should be 1')
else:
    print('the bit should be 0')


