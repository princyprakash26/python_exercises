# names that reached number one:

def name_read():

    boys_name=input('enter the boys filename:')
    girls_name=input('enter the girls filename:')

    with open(boys_name, 'r') as fb :
        boy_name=fb.readlines()

    with open(girls_name, 'r') as fg:
        girl_name=fg.readlines()

    print('Boys name')
    print('**********')

    for names in boy_name:
        print(names)

    print('Girls name')
    print('***********')

    for name in girl_name:
        print(name)

name_read()