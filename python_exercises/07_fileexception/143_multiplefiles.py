# concanate multiple files

def multi_files():
    while True:
        f = input('enter the filename:')
        if f == '' :
            break
        try:
            with open(f , 'r') as f:
                reading = f.read()
                print(reading)

        except FileNotFoundError:
            print('enter a correct filename:')
        
        
            
        
multi_files()
        

    
    