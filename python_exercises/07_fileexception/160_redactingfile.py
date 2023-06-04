# redacting text in a file:

def redact():

    f = input('enter the input filename:')


    with open(f ,'r') as f:
        text = f.read()
        redacted = text.replace('fear','****')
        redacted = redacted.replace('tried' , '*****')
        redacted = redacted.replace('fall' , '****')
        print(redacted)
    
    sensis = input('enter the output filename:')
    with open(sensis , 'w') as sensis:
        sensi = sensis.write(redacted)

        print(sensis)

redact()
        