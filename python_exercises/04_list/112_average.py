#below and above average:
def average_above_below():
    numbers = []
    
    while True:
        number = input('Enter a number (press Enter to stop): ')
        if number == '':
            break 
        numbers.append(int(number))  
    average = sum(numbers) // len(numbers)  # Calculate the average
    
    above_average = []
    below_average = []
    
    for num in numbers:
        if num > average:
            above_average.append(num)
        elif num < average:
            below_average.append(num)
    
    return 'average:',average,'belowaverage:',below_average,'above average:',above_average
      
report = average_above_below()
print(report)
