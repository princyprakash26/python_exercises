#what colour is that square:

square = input("Enter the square coordinates : ")

column = square[0].lower()
row = int(square[1])
sum_value = ord(column) + row

print(ord(column))                                  # coverts character into integer :
print(sum_value)

if sum_value % 2 == 0:
    color = "black"
else:
    color = "white"

print(f"The square {square} is {color}.")
