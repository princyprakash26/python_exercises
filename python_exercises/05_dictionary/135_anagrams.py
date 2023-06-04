# anagrams

def is_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    # Check if the lengths are different
    if len(word1) != len(word2):
        return False

    # Convert the words to lists of characters
    chars1 = list(word1)
    chars2 = list(word2)

    chars1.sort()
    chars2.sort()
    return chars1 == chars2

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")

