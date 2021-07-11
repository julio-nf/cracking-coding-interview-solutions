class Stack():
    def __init__(self):
        self._stack = []

    def push(self, value: int) -> None:
        self._stack.append(value)

    def pop(self) -> int:
        if len(self._stack) != 0:
            return self._stack.pop()

    def peek(self) -> int:
        if len(self._stack) != 0:
            return self._stack[-1]

    def is_empty(self) -> bool:
        return len(self._stack) == 0


def sort_stack(stack: Stack) -> Stack:
    aux_stack = Stack()
    while not stack.is_empty():
        aux = stack.pop()

        while not aux_stack.is_empty() and aux_stack.peek() > aux:
            stack.push(aux_stack.pop())

        aux_stack.push(aux)

    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())

    return stack


if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(7)
    stack = sort_stack(stack)
