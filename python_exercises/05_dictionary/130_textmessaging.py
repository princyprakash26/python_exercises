# text messaging
dictionary = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQR',
    '8': 'STU',
    '9': 'VWXYZ',
    '0': ''
}

user_input = input('Enter a string: ')
output = ''

for char in user_input:
    for key, value in dictionary.items():
        if char.upper() in value:
            output += key
print(output)
