# sorted order:


def order():
    orders = []  
    while True:
        order = int(input('Enter a value: '))
        if order != 0:
            orders.append(order)  
            print("order:", order)
        else:
            break
    
    sorted_orders = sorted(orders)  
    print( sorted_orders)  
order()

