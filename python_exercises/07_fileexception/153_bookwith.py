# a book with no 'e' :


def No_e():
    input_file=input('enter the filename:').lower()


    with open(input_file, 'r') as f:
        text=f.read()
        count = text.count('e')
        print('count of e:',count)
        if count > 0 :
            result=text.replace('e','')
            print('without e:',result)

No_e()