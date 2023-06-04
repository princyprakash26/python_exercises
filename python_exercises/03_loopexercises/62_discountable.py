#discount table:

new_prices=[4.95,9.95,14.95,19.95,24.95]

for prices in new_prices:
    discount = prices * 0.6
    new_prices = prices - discount
print(discount, "\n", new_prices)
