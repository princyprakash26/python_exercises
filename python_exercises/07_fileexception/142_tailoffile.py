#display the tail of the file:

def tail_of_file():
    get=input('enter the filename:')
    try:
        with open(get,'r') as get:
            text=get.readlines()
            tail=text[-5:]
            for lines in tail:
                print(lines)
    except FileNotFoundError:
        print('files is not found')

tail_of_file()