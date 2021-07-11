class MyQueue():
    def __init__(self):
        self.newest = []
        self.oldest = []

    def _shift_stacks(self):
        while len(self.newest) != 0:
            self.oldest.append(self.newest.pop())

    def add(self, value):
        self.newest.append(value)

    def peek(self):
        self._shift_stacks()
        return self.oldest[-1]

    def remove(self):
        self._shift_stacks()
        return self.oldest.pop()

    def isEmpty(self):
        return len(self.newest) + len(self.oldest) == 0


if __name__ == '__main__':
    queue = MyQueue()
    queue.add(2)
    queue.add(5)
    queue.add(8)
    queue.add(3)
    queue.add(1)
    x = queue.remove()
    x = queue.remove()
    x = queue.remove()
    x = queue.remove()
