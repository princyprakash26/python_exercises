#negative ,zeros and positives:

def neg_zero_pos():
    emp =[]
    while True:
        read=input('enter the values:')
        if read =='':
            break
        value = int(read)
        emp.append(value)
    emp.sort()
    return emp

result = neg_zero_pos()
print(result)
