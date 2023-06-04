# center a string in the terminal:

def  center_string(box,width):
    string=box
    count=string.count(string)
    print(count)
    return string 
string="hello world"
center_string(string,20)
print(string.center(120))

print('\t')