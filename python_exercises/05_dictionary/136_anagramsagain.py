# anagrams again

import string

def charactercounts(s):
    count = {}
    s1 = s.lower().replace(' ', '')
    punctuation = string.punctuation

    for ch in s1:
        if ch in punctuation:
            continue
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    return count

def main():
    s1 = input('enter the first string:')
    s2 = input('enter the second string')
    counts1 = charactercounts(s1)
    counts2 = charactercounts(s2)

    if counts1 == counts2:
        print('those strings are anagrams')
    else:
        print('it is not')


if __name__ == "__main__":
    main()

