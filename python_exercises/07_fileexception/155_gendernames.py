# gender neutral names:

def find_gender_neutral_names():
    year = input("Enter the year: ")

 
    with open(f"boys_{year}.txt", 'r') as boys_file:
        boys_names = boys_file.read().splitlines()

   
    with open(f"girls_{year}.txt", 'r') as girls_file:
        girls_names = girls_file.read().splitlines()
      

    gender_neutral_names = set(boys_names) & set(girls_names)
 
    if len(gender_neutral_names) > 0:
        print("Gender-neutral names:")
        for name in gender_neutral_names:
            print(name)
    else:
        print("No gender-neutral names found for the specified year.")

find_gender_neutral_names()
