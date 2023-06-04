#Faces on money:

individual={
    '$1':'George washington',
    '$2':'Thomas Jefferson' ,
    '$5':'Abraham Lincoln',
    '$10':'Alexander Hamilton'  ,
    '$20':'Andrew Jackson' ,
    '$50':'Ulysses S.Grant',
    "$100":'Benjamin Franklin' 
}

money=input("Enter the denominations of banknote:")

if money in individual:
    denomination=individual[money]
    print(denomination)
else:
    print("enter the valid denominations")