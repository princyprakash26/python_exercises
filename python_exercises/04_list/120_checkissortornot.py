# Is a list already in sorted order:

def sortorder(lists):
    return lists==sorted(lists) or lists==sorted(lists,reverse=True)
  
    

def main():
    lists=[1,2,3,4,5]
    result=sortorder(lists)
    print(result)

main()


