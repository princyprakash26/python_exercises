# numbers to english:

numwords = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
}

def number_to_words(number):
    if number < 0:
        return 'minus ' + number_to_words(abs(number))

    if number < 20:
        return numwords[number]

    if number < 100:
        tens = number // 10 * 10
        ones = number % 10
        if ones:
            return numwords[tens] + '-' + numwords[ones]
        else:
            return numwords[tens]

    if number < 1000:
        hundreds = number // 100
        remainder = number % 100
        if remainder:
            return numwords[hundreds] + ' hundred and ' + number_to_words(remainder)
        else:
            return numwords[hundreds] + ' hundred'

    if number < 1000000:
        thousands = number // 1000
        remainder = number % 1000
        if remainder:
            return number_to_words(thousands) + ' thousand ' + number_to_words(remainder)
        else:
            return number_to_words(thousands) + ' thousand'

   

    return 'number out of range'


number = int(input('Enter a number: '))
words = number_to_words(number)
print(f'{number} in words: {words}')
