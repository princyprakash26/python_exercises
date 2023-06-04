#frequency to note:

frequency_notes = {
    261.63: 'C4',
    293.66: 'D4',
    329.63: 'E4',
    349.23: 'F4',
    392.00: 'G4',
    440.00: 'A4',
    493.88: 'B4'
}


frequency = float(input("Enter the frequency (in Hz): "))

if frequency in frequency_notes:
    note = frequency_notes[frequency]
    print("The note corresponding to", frequency, "Hz is", note)
else:
    print("No note found for the given frequency.")
