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


def return_kth_to_last(linked_list: LinkedList, k: int) -> Node:
    i = linked_list.head
    j = linked_list.head

    for _ in range(k + 1):
        if i is None:
            return i
        i = i.next

    while i is not None:
        i = i.next
        j = j.next

    return j


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    print(return_kth_to_last(linked_list, 0).value)
