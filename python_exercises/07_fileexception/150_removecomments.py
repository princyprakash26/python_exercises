import os
def removecomments():
    inread=input('enter the filename:')
    try:
        with open(inread,'r') as inread :
            for line in inread :
                if '#' in line:
                    line = line.replace('#','***')
                print(line)
    except FileNotFoundError:
        print('invalid filename')

    newname=input('enter the newfilename:')
    os.rename(inread.name ,newname)

    
removecomments()
