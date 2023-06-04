
def run_length_decode(encoded_list):
    if len(encoded_list) == 0:
        return []

    value = encoded_list[0]
    count = encoded_list[1]
    decoded_list = [value] * count

    remaining_list = encoded_list[2:]
    return decoded_list + run_length_decode(remaining_list)

# Main program
def main():
    encoded_list = ['A', 3, 'B', 2, 'C', 4, 'D', 1]  
    decoded_list = run_length_decode(encoded_list)
    
    print(encoded_list)
    print(decoded_list)

main()
