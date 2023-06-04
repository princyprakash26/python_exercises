# grade points average:

letter = []
while True:
    grade = input('enter the grade:').upper()
    if grade == '' :
        break

    if grade == 'A+' or grade == 'A':
        value = 4.0
    elif grade == 'A-' :
        value = 3.7
    elif grade == 'B+' :
        value = 3.3
    elif grade == 'B' :
        value = 3.0
    elif grade == 'B-':
        value = 2.7
    elif grade == 'C+':
        value = 2.3
    elif grade == 'D+':
        value = 1.7
    elif grade == 'D':
        value = 1.3
    elif grade == 'F' :
        value = 1.0
    else:
        value = 0
      
    letter.append(value)

result = sum(letter) / len(letter)
print('average:',result)