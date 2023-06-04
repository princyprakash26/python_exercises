 # words that occur most:

def words():
    with open('sixvowels.txt'.lower(), 'r') as f:
        text = f.read().split()
        
    word_counts = {}
    
    for word in text:
        word = word.lower()
        word = word.strip('!,')
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    if len(word_counts) > 0:
        common_word = max(word_counts)
        count = word_counts[common_word]
        print(f"The word that occurs most :'{common_word}' with a count of :{count}.")
    else:
        print("No words found.")

words()

