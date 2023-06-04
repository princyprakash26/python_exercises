# # only the words:


def words(string):
    result = []
    
    words = string.split()
    
    for i in words:
        i = i.strip(',".:')


        result.append(i)
    
    return result


def main():
    text = input('Enter the string: ')
    output = words(text)
    print(output)


main()
