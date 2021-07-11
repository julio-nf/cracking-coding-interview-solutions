class StackOfPlates():
    def __init__(self, max: int) -> None:
        self.stacks = {}
        self.max = max
        self.total_len = 0

    def _get_last_stack(self) -> list[int]:
        if len(self.stacks) == 0:
            return None

        return self.stacks[len(self.stacks) - 1]

    def push(self, value: int) -> None:
        stack = self._get_last_stack()

        if stack is None or len(stack) == self.max:
            new_stack = [value]
            self.stacks[len(self.stacks)] = new_stack
        else:
            stack.append(value)

    def pop(self) -> int:
        stack = self._get_last_stack()

        if stack is None:
            return None

        element = stack.pop()

        if len(stack) == 0:
            self.stacks.pop(len(self.stacks) - 1)

        return element


if __name__ == '__main__':
    stack = StackOfPlates(3)
    stack.push(3)
    stack.push(2)
    stack.push(4)
    stack.push(7)
    stack.push(9)
    stack.push(8)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
