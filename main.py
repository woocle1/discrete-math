import binaryTree as tree
from orientation import graphOrientation
from execute import executeReversedPolska
from expressionToPolska import expressionToPolska


def main():
    matrix = [[0, 1, 0, 1, 0],
              [1, 1, 0, 1, 0],
              [0, 0, 0, 1, 1],
              [0, 0, 0, 0, 1],
              [1, 1, 0, 0, 1]]
    print(graphOrientation(matrix))
    expression = "( 11 + 19 ) / ( 8 / 4 - 1 )"
    polska = expressionToPolska(expression)
    binTreeRoot = tree.polskaToBinaryTree(polska)

    print("Вираз:" + expression.replace(' ', ''))

    tree.printTree(binTreeRoot, None, False)

    print("Симетричний обхід дерева: ", end="")
    tree.symmetricalOrderTraversal(binTreeRoot)

    print("\nПрямий обхід дерева (прямий польський запис): ", end="")
    tree.directOrderTraversal(binTreeRoot)

    print("\nЗворотній обхід дерева (зворотній польський запис): ", end="")
    tree.reversedOrderTraversal(binTreeRoot)

    print("\nВираз за зворотнім польським записом: ")
    executeReversedPolska(polska)


if __name__ == "__main__":
    main()