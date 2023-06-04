dollars = float(input("Enter the number of dollars:\n"))
cents = float(input("Enter the number of cents:\n"))

amount = dollars + 100 * cents
TOONIES = 0
LOONIES = 0
QUARTERS = 0
DIMES = 0
NICKELS = 0
PENNIES = 0

while amount >= 200:
  amount -= 200
  TOONIES += 1
while amount >= 100:
  amount -= 100
  LOONIES += 1
while amount >= 25:
  amount -= 25
  QUARTERS += 1
while amount >= 10:
  amount -= 10
  DIMES += 1
while amount >= 5:
  amount -= 5
  NICKELS += 1
while amount >= 1:
  amount -= 1
  PENNIES += 1
print(f"You need  {TOONIES}  toonies,  {LOONIES}  loonies,  {QUARTERS} quarters, {DIMES}, dimes {NICKELS}  nickels, and {PENNIES} pennies.")