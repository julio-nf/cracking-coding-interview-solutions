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


def append_node(new_node: Node, tail_node: Node) -> Node:
    tail_node.next = new_node
    return tail_node.next


def partition_linked_list(partition: int, linked_list: LinkedList) -> Node:
    current = linked_list.head
    less_head = None
    less_tail = None
    greater_head = None
    greater_tail = None

    while current is not None:
        new_node = Node(current.value)
        if current.value < partition:
            if less_head is not None:
                less_tail = append_node(new_node, less_tail)
            else:
                less_head = new_node
                less_tail = less_head
        else:
            if greater_head is not None:
                greater_tail = append_node(new_node, greater_tail)
            else:
                greater_head = new_node
                greater_tail = greater_head

        current = current.next

    less_tail.next = greater_head

    return less_head


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(8)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(1)
    partitioned_linked_list = partition_linked_list(5, linked_list)
    linked_list.print_list(partitioned_linked_list)
