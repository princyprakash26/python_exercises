# two dice stimulation:

import random

total_counts = [0] * 13  

for j in range(1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(total)
    total_counts[total] += 1
    print(total_counts)


total_percentages = [count / 1000 * 100 for count in total_counts]


print("Total\tOccurrences\tExpected Probability")

for i in range(2, 13):
    expected_probability = (i == 7) * 1/6 + (i == 6 or i == 8) * 5/36 + (i == 5 or i == 9) * 1/9
    print(f"{i}\t{total_counts[i]}\t{expected_probability * 100:.2f}%")
