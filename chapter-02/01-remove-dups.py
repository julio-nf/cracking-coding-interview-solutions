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


def remove_dups(linked_list: LinkedList) -> LinkedList:
    dups = {}

    before = None
    current = linked_list.head
    while current is not None:
        if current.value in dups:
            before.next = current.next
        else:
            dups[current.value] = True
            before = current
        current = current.next

    return linked_list


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(4)
    remove_dups(linked_list)
    linked_list.print_list(linked_list.head)
