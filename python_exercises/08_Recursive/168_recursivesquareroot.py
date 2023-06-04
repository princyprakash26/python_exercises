#recursive square root:


def square_root(n, guess =1.0):
    difference = guess * guess - n
    if difference < 0:
        difference = -difference
    if difference < 0.0001:
        return guess
    else:
        new_guess = (guess + n / guess) / 2
        return square_root(n, new_guess)

number = float(input("Enter the number: "))
square = square_root(number)
print(square)




