# words with six vowels in orders:


def wordswithsixvowels():
    filename = input('Enter the filename: ').lower()

    try:
        with open(filename, 'r') as f:
            text = f.read()
            print(text)
           
        for i in range(len(text) - 5):
            if (
                text[i] in 'aeiou'
                and text[i + 1] in 'aeiou'
                and text[i + 2] in 'aeiou'
                and text[i + 3] in 'aeiou'
                and text[i + 4] in 'aeiou'
                and text[i + 5] in 'aeiou'
            ): 
                print(text[i + 5])
                print('Words with six vowels in order found.')
                break
        else:
            print('No words with six vowels in order found.')

    except FileNotFoundError:
        print('File not found.')


wordswithsixvowels()
