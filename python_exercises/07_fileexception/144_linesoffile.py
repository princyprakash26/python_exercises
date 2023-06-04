#lines of file

def number_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines,1):
                print(f"{i}: {line}")
    except FileNotFoundError:
        print("File not found.")

filename = input("Enter the filename: ")
number_lines(filename)
