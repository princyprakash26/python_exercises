meal_rs = int(input("Enter the amount of your meal:"))

sales_tax = 0.07
tiprate = 0.18
tax_amount = meal_rs * sales_tax
meal_tips = meal_rs * tiprate
total = meal_rs + meal_tips + tax_amount

print(meal_rs)
print(tax_amount)
print(meal_tips)
print(total)