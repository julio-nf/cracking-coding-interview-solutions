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


def check_palindrome(linked_list: LinkedList) -> bool:
    stack = []
    slow = linked_list.head
    fast = linked_list.head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        stack.append(slow.value)
        slow = slow.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        if slow.value != stack.pop():
            return False

        slow = slow.next

    return True


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_end('t')
    linked_list.insert_at_end('a')
    linked_list.insert_at_end('c')
    linked_list.insert_at_end('o')
    linked_list.insert_at_end('c')
    linked_list.insert_at_end('a')
    linked_list.insert_at_end('t')

    print(check_palindrome(linked_list))
