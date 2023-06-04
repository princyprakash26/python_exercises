# consistent line lengths:


def linelengths(maxlength=80):
    input_file = input('enter the input file name:')

    with open(input_file, 'r') as input_file :
        for line in input_file :
            if len(line) > maxlength:
                print(line[:maxlength])
                line=line[maxlength:]
                
            print(line)

linelengths()