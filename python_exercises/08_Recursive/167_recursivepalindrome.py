#Recursive palindrome:

def palindrome():
    string = input("Enter the string:")

    if string =='':
        print("It is palindrome")
    elif string ==" ":
        print("Single letter is also a palindrome.")
    elif string == string[::-1]:
        print("The string is palindrome")
    else :
        print("Trhe string is not a palindrome")
        return palindrome() + string
palindrome()

