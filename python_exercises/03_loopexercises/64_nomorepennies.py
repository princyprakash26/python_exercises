# no more pennies:

pennies_nickel = 5
nickel = 0.5

total = 0.00

while True :
    price = input('enter the price:')
    if price == '':
        break
    total = total + float(price)
print(f'the amount is {round(total, 2)}')
rounding = total * 100 % pennies_nickel
if rounding < pennies_nickel /2:
    cash = total - rounding/100
else:
    cash = total + nickel - rounding/100

print('cash:',cash)

