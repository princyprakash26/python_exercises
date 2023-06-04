# sum of list of numbers:

def sum_of_lists():
    values = []
    try:
        num_values = int(input("Enter the number of values: "))

        for _ in range(num_values):
            value = int(input("Enter a value: "))
            values.append(value)

        sum_of_numbers = sum(values)
        print("Sum of numbers:", sum_of_numbers)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

sum_of_lists()

