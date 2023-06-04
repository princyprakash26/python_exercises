# missing comments:

def missingcomments():
    input_file = input('Enter the filename: ')

    try:
        with open(input_file, 'r') as f:
            text = f.read().splitlines()

        if len(text) > 0 and not text[0].startswith('#'):
            print('Missing comment in the first line.')

        else:
            print('comment line is present before the function')

    except FileNotFoundError:
        print('File not found.')


missingcomments()
