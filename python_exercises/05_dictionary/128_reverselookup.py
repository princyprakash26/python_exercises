# reverse lookup

def reverselookup(dictionary, value):
    keys = []

    for key in dictionary:
        if dictionary[key] == value:
            keys.append(key)

    return keys

def main():
    dictionary = {
        'fruit' : 'apple',
        'book' : 'paper',
        'orange' : 'apple',
        }
    print('the reverselookup:',reverselookup(dictionary, 'apple'))

if __name__ == "__main__":
    main()
