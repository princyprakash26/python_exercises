word = input('Enter the word: ')
word = word.strip().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
punc = [',', '!', '?']
new_word = ''

if word[-1] in punc:
    last_char = word[-1]
    word = word[:-1]
else:
    last_char = ''

if word[0] in vowels:
    new_word = word + 'way' + last_char
else:
    for i in range(len(word)):
        if word[i] in consonants:
            new_word = word[i:] + word[:i] + 'ay' + last_char
            break

new_word = new_word.capitalize()
print(new_word)
