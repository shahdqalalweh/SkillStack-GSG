# Convert infix expression to postfix (Reverse Polish Notation)

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    # Split the expression into tokens (numbers, operators, parentheses)
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isnumeric():  # If token is a number
            output.append(token)
        elif token == '(':  # Opening parenthesis
            stack.append(token)
        elif token == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from the stack
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    # Pop any remaining operators from the stack
    while stack:
        output.append(stack.pop())

    return ' '.join(output)

# Example usage
expr = "( 1 + 2 ) * 3"
result = infix_to_postfix(expr)
print("Postfix Expression:", result)
