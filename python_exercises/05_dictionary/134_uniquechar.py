# unique characters:

text =  input('enter the string:')

char = {}

for ch in text:
    char[ch] = char.get(ch, 0)

print(f'the string:{len(char)},unique characters')