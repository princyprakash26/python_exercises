def repeatedwords():
    try:
        with open('repeatedwords.txt', 'r') as f:
            text = f.read().split()
            print(text)
        repeated_words = []

        for word in text:

            if text.count(word) > 1 :
                repeated_words.append(word)

        if len(repeated_words) > 0:
            print('Repeated words:')
            for word in repeated_words:
                print(word)
        else:
            print('No repeated words found.')

    except FileNotFoundError:
        print('Invalid input.')

repeatedwords()


