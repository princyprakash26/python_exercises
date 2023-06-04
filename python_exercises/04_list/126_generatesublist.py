# generate all sublist of a list:

def isSublist():
    lists=[1,2,3]
    num=[]
    for i in range(len(lists)):
        for j in range(i+1,len(lists)+1):
            num.append(lists[i:j])
            print(num)                           

    return num

result=isSublist()
print(result)

    