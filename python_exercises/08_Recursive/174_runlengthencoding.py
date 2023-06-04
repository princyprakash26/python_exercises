
def run_length_encode(data):
    if len(data) == 0:
        return []

    count = 1
    current = data[0]
    encoded_list = []

    for i in range(1, len(data)):
        if data[i] == current:
            count += 1
        else:
            encoded_list.append(current)
            encoded_list.append(count)
            current = data[i]
            count = 1

    encoded_list.append(current)
    encoded_list.append(count)

    return encoded_list

# Main program
def main():
    string = input("Enter a string of characters: ") 
    data = list(string)  
    encoded_list = run_length_encode(data)

    print( data)
    print(encoded_list)

main()

