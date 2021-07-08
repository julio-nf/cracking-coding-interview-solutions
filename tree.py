class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree():
    # O(log n) where n is number of nodes
    def insert_node(self, node: Node, value):
        if node is None:
            return Node(value)

        if value == node.value:
            return 'Value already exists'
        elif node.value > value:
            node.left = self.insert_node(node.left, value)
        else:
            node.right = self.insert_node(node.right, value)

        return node

    def search_value(self, node: Node, value):
        if node is None or node.value == value:
            return node.value
        elif node.value > value:
            return self.search_value(node.left, value)
        else:
            return self.search_value(node.right, value)

    # O(n) where n is number of nodes
    def print_tree(self, node):
        if node:
            self.print_tree(node.left)
            print(node.value)
            self.print_tree(node.right)


if __name__ == '__main__':
    root = None
    tree = Tree()
    root = tree.insert_node(root, 4)
    tree.insert_node(root, 13)
    tree.insert_node(root, 7)
    tree.insert_node(root, 21)
    print(tree.search_value(root, 21))
