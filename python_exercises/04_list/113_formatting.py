# formatting a list:
def formatting(lists):
    result = []
    for i in range(len(lists)):
        if i == len(lists) - 1:
            result.append(' and '.join(lists[:i+1]))  # Added spaces around 'and'
        else:
            result.append(', '.join(lists[:i+1]))  # Removed 'and'

    return result

def main():
    lists = ['apple', 'mango', 'orange']
    report = formatting(lists)
    for item in report:
        print(item)

main()


