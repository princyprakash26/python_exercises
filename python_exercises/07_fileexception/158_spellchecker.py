# spell checker

def spellchecker():
    known_words = ['spell', 'exam', 'learn', 'check']

    input_file = input('Enter the filename: ')

    try:
        with open(input_file, 'r') as f:
            text = f.read().splitlines()
            text = list(set(text))

        incorrect_words = []

        for word in text:
            if word.lower() not in known_words:
                incorrect_words.append(word)

        if len(incorrect_words) > 0:
            print('Incorrect words:')
            for word in incorrect_words:
                print(word)
        else:
            print('All words are correct.')

    except FileNotFoundError:
        print('Invalid input.')

spellchecker()

