# pig latin

word = input('enter the word:')

word = word.strip().lower()
consonant = 'ay'
vowel = 'way'
piglatin = ''
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(word)):
    if word[i] in vowels:
        if i==0 :
            word += 'w'
        piglatin += word[i:] + word[0:i] + 'ay'
        break
print(piglatin)
print(word[i:])
print(word[0:i])
