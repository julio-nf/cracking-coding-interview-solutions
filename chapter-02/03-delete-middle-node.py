class Node():
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        new_node = Node(value)
        node.next = new_node

    def print_list(self, node):
        if node is None:
            return

        print(node.value)
        self.print_list(node.next)


def delete_middle_node(middle: Node) -> Node:
    if middle is None or middle.next is None:
        return None

    next_node = middle.next
    middle.value = next_node.value
    middle.next = next_node.next

    return middle


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(1)
    node = linked_list.head
    while node.next is not None:
        node = node.next
    new_node = Node(2)
    node.next = new_node
    linked_list.insert_at_end(4)
    linked_list.print_list(linked_list.head)
    delete_middle_node(new_node)
    linked_list.print_list(linked_list.head)
