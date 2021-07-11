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


def calculate_sum_and_rest(rest: int, *values: int):
    values_sum = sum(x for x in values)
    new_value = 0

    if values_sum >= 10:
        subtracted = (10 - values_sum) * -1
        new_value = subtracted + rest
        rest = 1
    else:
        new_value = values_sum + rest
        rest = 0

    return new_value, rest


def sum_linked_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    head = None
    tail = None

    current_l1 = ll1.head
    current_l2 = ll2.head
    sum_rest = 0
    while current_l1 is not None or current_l2 is not None:
        new_value, sum_rest = calculate_sum_and_rest(
            sum_rest, current_l1.value, current_l2.value
        )

        if head is None:
            head = Node(new_value)
            tail = head
        else:
            tail.next = Node(new_value)
            tail = tail.next

        current_l1 = current_l1.next
        current_l2 = current_l2.next

    if sum_rest > 0:
        tail.next = Node(sum_rest)

    return head


if __name__ == '__main__':
    linked_list_1 = LinkedList()
    linked_list_1.insert_at_end(3)
    linked_list_1.insert_at_end(9)
    linked_list_1.insert_at_end(5)
    linked_list_2 = LinkedList()
    linked_list_2.insert_at_end(2)
    linked_list_2.insert_at_end(1)
    linked_list_2.insert_at_end(6)

    sum_list = sum_linked_lists(linked_list_1, linked_list_2)
    linked_list_1.print_list(sum_list)
