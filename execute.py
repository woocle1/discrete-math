def executeReversedPolska(polskaExpression):
    stack = []
    iterator = 1
    for token in polskaExpression.split():
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
            print(str(iterator) + ") " + str(a) + " + " + str(b) + " = " + str(a + b))
            iterator += 1

        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
            print(str(iterator) + ") " + str(a) + " - " + str(b) + " = " + str(a - b))
            iterator += 1

        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
            print(str(iterator) + ") " + str(a) + " * " + str(b) + " = " + str(a * b))
            iterator += 1

        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
            print(str(iterator) + ") " + str(a) + " / " + str(b) + " = " + str(a / b))
            iterator += 1

        elif token == "^":
            b = stack.pop()
            a = stack.pop()
            stack.append(pow(a, b))
            print(str(iterator) + ") " + str(a) + " ^ " + str(b) + " = " + str(pow(a, b)))
            iterator += 1

        elif token.isdigit():
            stack.append(float(token))
    print("Відповідь: " + str(stack.pop()))

