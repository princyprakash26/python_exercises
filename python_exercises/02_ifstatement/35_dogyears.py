#Dog years:
human_age = int(input("Enter the human age in years: "))

if human_age <= 0:
    print("Invalid input. Please enter a positive number.")
elif human_age <= 2:
    dog_age = 10.5
else:
    dog_age = 21 + (human_age - 2) * 4

print( dog_age, "years")

