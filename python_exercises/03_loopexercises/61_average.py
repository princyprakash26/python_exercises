# average

count = int(input("Enter the number of values: "))  
total = 0
if count == 0:
    print("0")
else:
    for i in range(count):
        value = float(input("Enter a value: ")) 
        total += value
    print(total)
    average = total / count

    print( average)


