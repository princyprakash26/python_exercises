# day old bread:

purchased = float(input('enter the number of bread is purchased:'))
bread = 3.49
discount = 0.60

total_price = purchased * bread
Discount_price = total_price -(total_price -discount)

print('total price:$', round(Discount_price, 2))