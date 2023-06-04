# display the head of the file:
def head_of_file():
    a=input('enter the file name:')
    try:
        with open(a,'r') as a :
            text=a.readline()          # this will read only single line of the file
            print(text)
    except FileNotFoundError:
        print('file not found')

head_of_file() 


   
