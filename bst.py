class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.value)


class BST(object):
    def __init__(self):
        self.root = None
        self.comparisons = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

        else:
            current = self.root

            while True:
                if value < current.value:
                    self.comparisons += 1

                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break

                elif value > current.value:
                    self.comparisons += 1

                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break

                else:
                    break

    def find(self, value):
        if self.root is None:
            return None

        else:
            current = self.root

            while True:
                if current.value == value:
                    return current
                elif current.left and current.value > value:
                    self.comparisons += 1
                    current = current.left
                elif current.right and current.value < value:
                    self.comparisons += 1
                    current = current.right
                else:
                    return None

    def breadth_first_tree(self):
        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while queue:
            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

            out.append(str(current_node.value) + " ")

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        print "".join(out)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value)
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node:
            print(node.value)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(self.value)


if __name__ == '__main__':
    t = BST()

    t.insert(7)
    t.insert(6)
    t.insert(5)

    for i in xrange(10000):
        t.insert(i)

    print(t.comparisons)
