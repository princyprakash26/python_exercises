#median of three values:

def median(a,b,c):
    list=[]
    list.append(a)
    list.append(b)
    list.append(c)
    list.sort()
    medi=list[1]
    print(medi)
    return list
   
def main():
    a=int(input('enter the value for a:'))
    b=int(input('enter the value for b:'))
    c=int(input("enter the value for c:"))
    values=median(a,b,c)
    print(values)
    
main()