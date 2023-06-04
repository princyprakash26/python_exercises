

#recursive Decimal to Binary:

def decimal_to_binary(n):
    
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


decimal = int(input("Enter a non-negative decimal number: "))
if decimal >= 0:
    binary = decimal_to_binary(decimal)
    print("Binary representation:", binary)
else:
    print("Error:Enter the positive integer.")


