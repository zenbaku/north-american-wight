from bst import BST
from bst import Node


class RBST(BST):
    def __init__(self):
        super(RBST, self).__init__()

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)


if __name__ == '__main__':

    rt = RBST()

    print(rt)
    print("Hola")

