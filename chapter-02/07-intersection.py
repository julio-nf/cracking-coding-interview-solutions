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


def get_list_tail_size(ll: LinkedList):
    current = ll.head
    length = 0

    while current != None:
        length += 1
        current = current.next

    return current, length


def advance_list_steps(steps: int, node: Node) -> Node:
    for _ in range(steps):
        node = node.next

    return node


def check_intersection(ll1: LinkedList, ll2: LinkedList) -> Node:
    ll1_tail, ll1_len = get_list_tail_size(ll1)
    ll2_tail, ll2_len = get_list_tail_size(ll2)

    if ll1_tail is not ll2_tail:
        return None

    ll1_head = ll1.head
    ll2_head = ll2.head
    if ll1_len < ll2_len:
        ll2_head = advance_list_steps(ll2_len - ll1_len, ll2_head)
    elif ll1_len > ll2_len:
        ll1_head = advance_list_steps(ll1_len - ll2_len, ll1_head)

    while ll1_head is not None or ll2_head is not None:
        if ll1_head is ll2_head:
            return ll1_head

        ll1_head = ll1_head.next
        ll2_head = ll2_head.next

    return ll1_head is ll2_head

    # shorter = ll1.head if ll1_len < ll2_len else ll2.head
    # longer = ll2.head if ll1_len < ll2_len else ll1.head

    # longer = advance_list_steps(abs(ll1_len - ll2_len), longer)

    # while shorter is not longer:
    #     shorter = shorter.next
    #     longer = longer.next

    # return shorter


if __name__ == '__main__':
    linked_list1 = LinkedList()
    linked_list1.insert_at_end(3)
    linked_list1.insert_at_end(1)
    linked_list1.insert_at_end(5)
    linked_list1.insert_at_end(9)
    node = linked_list1.head
    while node.next is not None:
        node = node.next
    new_node = Node(7)
    node.next = new_node
    linked_list1.insert_at_end(2)
    linked_list1.insert_at_end(1)

    linked_list2 = LinkedList()
    linked_list2.insert_at_end(4)
    linked_list2.insert_at_end(6)
    node = linked_list2.head
    while node.next is not None:
        node = node.next
    node.next = new_node

    print(check_intersection(linked_list1, linked_list2))

# 3 -> 1 -> 5 -> 9 \
#                    7 -> 2 -> 1
#           4 -> 6 /
