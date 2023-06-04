# letter frequencies:
f=input('enter the filenames:').lower()
frequencies=['a' ,'b' , 'c', 'd','e','f','g','h','j','i','k','l','m','n','o','p','q','r'
       ,'s','t','u','v','w','x','y','z']
with open(f,'r') as f :
    text=f.read()
    # print(text)

if f in frequencies:
    print('files is matched with letter frequencies')


    
print(text)


