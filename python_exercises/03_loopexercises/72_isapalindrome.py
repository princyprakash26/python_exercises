# Is a string a palindrome:

string=input("enter the string:")

for string in range(len(string)):
    if string==string[-1:0]:
        print('it is palindrome')
    else:
        print('it is not palindrome')
