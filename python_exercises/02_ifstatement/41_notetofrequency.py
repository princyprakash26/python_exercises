#note to frequency:

''' note -frequency
C4- 261.63
D4 - 293.66
E4 - 329.63
F4 - 349.63
G4 - 392.00
A4 - 440.00
B4 - 493.88
'''

note = input("Enter the note name: ")

letter = note[0].lower()
octave = int(note[1])

# Calculate the frequency for notes 
if letter == 'c':
    frequency = 261.63 / (2 ** (4 - octave))
elif letter == 'd':
    frequency = 293.66 / (2 ** (4 - octave))
elif letter == 'e':
    frequency = 329.63 / (2 ** (4 - octave))
elif letter == 'f':
    frequency = 349.23 / (2 ** (4 - octave))
elif letter == 'g':
    frequency = 392.00 / (2 ** (4 - octave))
elif letter == 'a':
    frequency = 440.00 / (2 ** (4 - octave))
elif letter == 'b':
    frequency = 493.88 / (2 ** (4 - octave))
else:
    print("Invalid note name.")

print(note, frequency)



