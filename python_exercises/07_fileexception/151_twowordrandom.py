# two word random password:
# import random

# def password():

#     with open('input.txt','r') as f:
#         word=f.read()
#         print(word)
#         if len(word) < 2 :
#             print('insufficient words')
    
    
#     word1 = random.choice(word)
#     word2 = random .choice(word)
#     for i in range(1,9):
#         password = word1 + word2 + str(random.randint(10,99))

  

#     print(password)

# password()


import random

def password():
    with open('input.txt', 'r') as f:
        words = f.read()

    if len(words) < 2:
        print("Insufficient words in the file.")
        return

    word1 = random.choice(words)
    word2 = random.choice(words)
    print(word1)
    print(word2)

  

    if word2 == word1:
        word2 = random.choice(words)

    print(word2)


    password = word1 + word2 + str(random.randint(1000,9999)) + str(random.randint(10,90))

    if len(password) > 8:
        password = password[:8]

    print( password)

password()
