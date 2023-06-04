# square root:

num = int(input('enter the numbers in square root:'))

n=int(input('enter the number of times iterate:'))

guess = float(input('enter the initial guess'))

for i in range(n):
    guess = (guess + num/guess)/2
print('square root:',guess)