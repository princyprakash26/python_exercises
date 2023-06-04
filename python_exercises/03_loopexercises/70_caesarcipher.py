# 70.caser cipher:

message = input('enter the messages:')
shift = int(input('enter the shift value:'))

new_message = ''

for char in message:
    if char >= 'a' and char <= 'z':
        word = ord(char) - ord('a')
        word = (word + shift) % 26
        new_char = chr(word+ ord('a'))
        new_message = new_message + new_char
        print(new_message)
    elif char >= 'A' and char <= 'z':
        word = ord(char) - ord('A')        
        word = (word+shift) % 26
        new_char = chr(word+ ord('A'))
        new_message = new_message + new_char
        print(new_message)
    else:
        new_message = new_message + char
        print(new_message)
