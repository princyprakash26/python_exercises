#shipping calculator:

first_item=10.95
each_item=2.95
def calculator(item):
    charge=first_item + (each_item * (item-1))
    return charge

def main():
    items=int(input("enter the amount of items:"))
    shipping=calculator(items)
    print(shipping)
main()