# evaluate postfix:

def evaluate_postfix(expression):
    value  = []

    for token in expression:
        if token.isdigit():
            value.append(int(token))
        else:
            
            operand2 = value.pop()
            operand1 = value.pop()

         
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '^':
                result = operand1 ** operand2

            value.append(result)


    return value[0]


postfix_expression = ['5', '2', '+', '3', '*']
result = evaluate_postfix(postfix_expression)
print(result)  
