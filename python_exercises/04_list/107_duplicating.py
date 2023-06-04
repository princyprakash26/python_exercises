# avoid duplicating:

def get_unique_words():
    words = set()  # Create an empty set to store unique words

    while True:
        read = input('Enter a word (press Enter to stop): ')
        if read == '':
            break  
        words.add(read)  
    return words
    print(words)

def main():
    uniquewords = get_unique_words()
    for words in uniquewords:
       print(words)

main()


