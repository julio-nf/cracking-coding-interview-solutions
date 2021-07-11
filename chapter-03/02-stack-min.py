class StackNode():
    def __init__(self, value, min):
        self.value = value
        self.min = min


class Stack():
    def __init__(self):
        self._stack = []

    def push(self, value: int) -> None:
        min = value
        if len(self._stack) != 0 and self.peek().min < min:
            min = self.peek().min

        new_node = StackNode(value, min)
        self._stack.append(new_node)

    def pop(self) -> int:
        if len(self._stack) != 0:
            return self._stack.pop().value

    def min(self) -> int:
        if len(self._stack) != 0:
            return self.peek().min

    def peek(self) -> StackNode:
        if len(self._stack) != 0:
            return self._stack[-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    print(stack.min())
    stack.pop()
    stack.pop()
    print(stack.min())
