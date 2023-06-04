# # find the longest word in a file:

with open('head.txt','r') as f:
    text=f.read()
    con=text.split()
    print(con)


length=[len(word) for word in con]
max_length=max(length)
print(length)

max_word = con[length.index(max_length)]

print(f"max_length:{max_length} for max_word:{max_word}")

