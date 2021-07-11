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


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.push(2)
    stack.push(3)
    print(stack.is_empty())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.peek())
    print(stack.pop())
