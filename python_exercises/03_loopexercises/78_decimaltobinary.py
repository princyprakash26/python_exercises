'''
result=''
q=input
for result in range(q=0):
set r= q%2
output=str(r)+result
q//2 =q
until q=0

'''

result=''
q = int(input('enter the decimal values:'))

while (q > 0):
    r = q%2
    result = str(r) + result
    q = q//2

print(result)