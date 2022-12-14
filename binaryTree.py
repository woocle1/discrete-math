class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'


def reversedOrderTraversal(root):
    if root is None:
        return
    reversedOrderTraversal(root.left)
    reversedOrderTraversal(root.right)
    print(str(root.data) + " ", end='')


def directOrderTraversal(root):
    if root is None:
        return
    print(str(root.data) + " ", end='')
    directOrderTraversal(root.left)
    directOrderTraversal(root.right)


def symmetricalOrderTraversal(root):
    if root is None:
        return
    symmetricalOrderTraversal(root.left)
    print(str(root.data) + " ", end='')
    symmetricalOrderTraversal(root.right)


def polskaToBinaryTree(polska):
    stack = []
    for token in polska.split():
        # если токен - оператор, то
        if isOperator(token):
            # извлекаем из стека два узла,
            y = stack.pop()
            x = stack.pop()
            # создаём новывй узел, в корне которого оператор, а в ветках два узла из стека,
            node = Node(token, x, y)
            # записываем полученый узел в стек
            stack.append(node)
        # если токен - число, то
        else:
            # создаём узел, в корне которого число, в ветках None, и записываем его в стек
            stack.append(Node(token))
    # возвращаем указатель на корень дерева
    return stack[-1]

class Trunk:
    def __init__(self, prev=None, str=None):
        self.prev = prev
        self.str = str


def showTrunks(p):
    if p is None:
        return
    showTrunks(p.prev)
    print(p.str, end='')


def printTree(root, prev, isLeft):
    if root is None:
        return

    prev_str = '    '
    trunk = Trunk(prev, prev_str)
    printTree(root.right, trunk, True)

    if prev is None:
        trunk.str = '—'
    elif isLeft:
        trunk.str = '.—'
        prev_str = '   |'
    else:
        trunk.str = '`—'
        prev.str = prev_str

    showTrunks(trunk)
    print(' ' + str(root.data))
    if prev:
        prev.str = prev_str
    trunk.str = '   |'
    printTree(root.left, trunk, False)