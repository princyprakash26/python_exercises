# random lottery numbers:

import random

def generate_lottery_numbers():
    lottery_numbers = []
    while len(lottery_numbers) < 6:
        number = random.randint(1, 50)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
        
    return lottery_numbers

def main():
    lottery_numbers = generate_lottery_numbers()
    print("Lottery Numbers:", lottery_numbers)

main()

