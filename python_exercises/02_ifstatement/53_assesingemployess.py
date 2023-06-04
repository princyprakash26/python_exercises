#Assessing employees.


rating = float(input('Enter the rating: '))

if rating >= 0.6:
    raise_percent = 0.05  # 5% raise for meritorious performance
elif rating >= 0.4:
    raise_percent = 0.03  # 3% raise for acceptable performance
else:
    raise_percent = 0.0   # No raise for unacceptable performance

salary = 2400.00  
new_salary = salary + (salary * raise_percent) 

print("$", new_salary)

