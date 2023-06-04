# remove outliers:


def remove_outliers():
    values = []
    
    while True:
        n = int(input("Enter a value (0 to stop): "))
        if n == 0:
            break
        values.append(n)
    
    if len(values) < 4:
        print("Insufficient values to remove outliers.")
        return values
    
    sorted_values = sorted(values)
    
    print(sorted_values)
    num_outliers = 2 
    
    outliers_removed = sorted_values[num_outliers:-num_outliers]
    return outliers_removed


def main():
    cleaned_values = remove_outliers()
    print("Values with outliers removed:", cleaned_values)


main()
