# compound interest:

deposit = float(input('enter the deposit amount'))
years = float(input('enter the saving for years:'))

amount = deposit * (1 + (4/100)) ** years
compound_interest = amount - deposit

print(amount)
print(compound_interest)