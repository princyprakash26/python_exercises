# possible changes

def check_coins(amount):
    quarter = 0.25
    dime = 0.10
    nickel = 0.05

    num_quarters = int(amount / quarter)
    amount -= num_quarters * quarter

    num_dimes = int(amount / dime)
    amount -= num_dimes * dime

    num_nickels = int(amount / nickel)
    amount -= num_nickels * nickel

    if amount == 0:
        return num_quarters, num_dimes, num_nickels
    else:
        return False

print(check_coins(1.4))

