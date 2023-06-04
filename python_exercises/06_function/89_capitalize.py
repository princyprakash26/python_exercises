# capitalize it

def capitalize_text(text):
    words = text.split()  # Split the text into individual words
    capitalized_words = []

    for word in words:
        if word.lower() == 'i':
            capitalized_words.append(word.upper())  # Handle 'i' as uppercase
        elif word.endswith('!') or word.endswith('.') or word.endswith('?'):
            capitalized_words.append(word[:-1] + word[-1].capitalize())

        else:
            capitalized_words.append(word.capitalize())  # Capitalize other words

    return ' '.join(capitalized_words)

    print(capitalize_words)

def main():
    text = input("Enter the text: ")
    result = capitalize_text(text)
    print(result)



main()

