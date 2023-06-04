# # the twelve days of christmas:

# def display_verse(verse_number):
#     days = [
#         "first", "second", "third", "fourth", "fifth",
#         "sixth", "seventh", "eighth", "ninth", "tenth",
#         "eleventh", "twelfth"
#     ]
    
#     gifts = [
#         "a partridge in a pear tree",
#         "two turtle doves",
#         "three French hens",
#         "four calling birds",
#         "five golden rings",
#         "six geese a-laying",
#         "seven swans a-swimming",
#         "eight maids a-milking",
#         "nine ladies dancing",
#         "ten lords a-leaping",
#         "eleven pipers piping",
#         "twelve drummers drumming"
#     ]
#     print("*********************************")
#     print(f"On the {days[verse_number-1]} day of Christmas,")
#     print("\n")
#     print(verse_number)


#     for i in range(verse_number-1,-1,-1):
#         if i == 0 and verse_number > 1:
#             print("And",'\t')
        
#         print(gifts[i])
    

# for verse_number in range(1, 13):
#     display_verse(verse_number)

    
#
def twelve_days(verse_number):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
            'eleventh', 'twelfth']
    verses = [
        "a partridge in a pear tree",
        "two turtle doves",
        "three French hens",
        "four calling birds",
        "five gold rings",
        "six geese a-laying",
        "seven swans a-swimming",
        "eight maids a-milking",
        "nine ladies dancing",
        "ten lords a-leaping",
        "eleven pipers piping",
        "twelve drummers drumming"
    ]

    print("*************************")
    print(f"On the {days[verse_number-1]} day of Christmas")
    print("my true love sent to me:")

    for i in range(verse_number-1, -1, -1):
        if i == 0 and verse_number > 1:
            print("And", '\t')
        
        print(verses[i])



# Print the lyrics for all twelve verses
for verse_number in range(1, 13):
    twelve_days(verse_number)
