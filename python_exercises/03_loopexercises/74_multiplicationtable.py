#Multiplication table:

n = int(input("enter the value of n:"))


for i in range(1,11):

    for i in range(1,11):
        print(f"{n*i}")
    n += 1
    print('\n',end='')
print(end='')