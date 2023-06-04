# what's that element again ?


def element():
    while True:
        input_file = input('Enter the element name: ')
        if input_file == '':
            break

        try:
            with open('elements.txt', 'r') as f:
                text = f.readlines()
            for line in text:
                elements = line.split()
                if input_file in elements:
                    print(elements)

        except FileNotFoundError:
            print('Invalid input')

element()
