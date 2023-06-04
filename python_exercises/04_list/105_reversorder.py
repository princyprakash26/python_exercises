#reverse order:
def reverse_order():
    emp =[]
    while True:
        read =int(input('enter the values:'))
        if read != 0:
            emp.append(read)
        else:
            break
    return emp

order=reverse_order()
order.reverse()
print(order)