#convert an integer to its ordinal number:
def integer_to_ordinalnumber(n):
    ordinalnumbers=['zero','one','two','three','four','five','six','seven','eight','nine']
    value=[]
    while n>0:
        num=n % 10
        # print(num)              #to check the flow:
        value.append(ordinalnumbers[num])
        n=n//10
    return value[::-1] 
number=1230
result=integer_to_ordinalnumber(number)
print(result)





