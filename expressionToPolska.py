from binaryTree import isOperator

def expressionToPolska(expression):
    polska = ""
    stack = []
    for token in expression.split():
        if token.isdigit():
            polska += str(token) + " "

        elif token == "(":
            stack.append(token)

        elif token == ")":

            while True:
                if stack[-1] == "(":
                    stack.pop()
                    break
                else:
                    polska += stack.pop() + " "

        elif isOperator(token):
            if len(stack) != 0:

                if isGreaterPriority(stack[-1], token):
                    polska += stack.pop() + " "
                stack.append(token)
            else:
                stack.append(token)
    while len(stack) != 0:
        polska += stack.pop() + " "
    return polska



def isGreaterPriority(token1, token2):
    operators = {"(": 0,
                 ")": 0,
                 "+": 1,
                 "-": 1,
                 "*": 2,
                 "/": 2,
                 "^": 3}
    try:
        if operators.get(token1) >= operators.get(token2):
            return True
        else:
            return False
    except TypeError:
        return False


