#count the elements:

def countrange(lists, minimum, maximum):
    count = 0

    for i in lists:
        count += 1

    print("Count:", count)

    if count <= maximum:
        return "Count is less than or equal to maximum"

    elif count >= minimum:
        return "Count is greater than or equal to minimum"

    return


def main():
    my_list = [1, 2, 3, 4, 5.5, 6]
    maximum_number = 6
    minimum_number = 4

    result = countrange(my_list, minimum_number, maximum_number)
    print(result)


main()

