def totalvalues():
    user_text = input("Enter the your text:")
    if user_text == (""):
        return 0
    else:
        return float(user_text) + totalvalues()
        

a = totalvalues()
print("Total value of the text:",a)


