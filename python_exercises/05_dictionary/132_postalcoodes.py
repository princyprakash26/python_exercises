#postalcodes:

postalcodes={
    'A' : 'Newfoundland' , 'B' : 'Nova scotia' , 'C' : 'Prince Edward Island' , 'E' :'New Brunswick' , 'G,H,J' :'Quebec' , 'K,L,M,N,P' : 'Ontario' , 'R' : 'Manitoba' ,
    'S' : 'Saskatchewan' , 'T' : 'Alberta' , 'V' : 'British Columbia' , 'X' : 'Northwest Territories' , 'Y' : 'Yukon'
}


user=input('enter the postal codes:')
output=''
for char in user:
    for key,values in postalcodes.items():
       if char.upper() in values:
           output += key
print(output)
