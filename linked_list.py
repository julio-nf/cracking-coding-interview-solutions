class Node():
    def __init__(self, value, next=None) -> None:
        self.next = next
        self.value = value


class LinkedList():
    def __init__(self) -> None:
        self.root = None

    def insert_at_end(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        node = self.root

        while node.next is not None:
            node = node.next

        new_node = Node(value)
        node.next = new_node

    def insert_at_end_recursive(self, node: Node, value):
        if node is None:
            self.root = Node(value)
            return
        elif node.next is None:
            node.next = Node(value)
            return

        self.insert_at_end_recursive(node.next, value)

    def print_list(self):
        node = self.root
        while node is not None:
            print(node.value)
            node = node.next

    def print_list_recursive(self, node):
        if node is None:
            return

        print(node.value)

        self.print_list_recursive(node.next)

    def search_value(self, value):
        if self.root is None:
            return 'List has no elements'

        current = self.root

        while current is not None:
            if current.value == value:
                return current.value
            current = current.next

        return 'Value not found'

    def search_value_recursive(self, node: Node, value):
        if node is None:
            return 'Value not found'
        elif node.value == value:
            return node.value

        return self.search_value_recursive(node.next, value)

    def delete_value(self, value):
        if self.root is None:
            return 'List has no elements'

        current = self.root
        last = None
        while current is not None:
            if current.value == value:
                if last is None:
                    self.root = current.next
                else:
                    last.next = current.next if current.next is not None else None

                return

            last = current
            current = current.next

        return 'Not found'


if __name__ == '__main__':
    list = LinkedList()
    list.insert_at_end_recursive(list.root, 5)
    list.insert_at_end_recursive(list.root, 7)
    list.insert_at_end_recursive(list.root, 9)
    list.insert_at_end_recursive(list.root, 11)
    list.print_list_recursive(list.root)
