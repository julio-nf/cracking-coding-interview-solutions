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


def check_loop(ll: LinkedList) -> Node:
    seen = {}
    current = ll.head

    while current not in seen or current is None:
        if current is None:
            return current

        seen[current] = True
        current = current.next

    return current


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    node = linked_list.head
    while node.next is not None:
        node = node.next
    new_node = Node(3)
    node.next = new_node
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    node = linked_list.head
    while node.next is not None:
        node = node.next
    node.next = new_node

    print(check_loop(linked_list))
