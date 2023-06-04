#infix to posix

def infix_to_postfix(expression):
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    operators = []
    postfix = []

  
    for token in expression:
        if token.isalnum():
           
            postfix.append(token)
        elif token == '(':
            
            operators.append(token)
        elif token == ')':
            
            while operators and operators[-1] != '(':
                postfix.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop() 
        else:
           
            while operators and operators[-1] != '(' and precedence[token] <= precedence.get(operators[-1], 0):
                postfix.append(operators.pop())
            operators.append(token)  

   
    while operators:
        postfix.append(operators.pop())

    return postfix
