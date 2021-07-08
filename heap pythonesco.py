class Heap():
    def __init__(self):
        self.size = 0
        self.heap = []

    def _father(self, i):
        return 0 if i == 0 else (i - 1) // 2

    def _left_child(self, i):
        return (2 * i) + 1

    def _right_child(self, i):
        return (2 * i) + 2

    def _min_child(self, i):
        left_child = self._left_child(i)
        right_child = self._right_child(i)

        min_child = i
        if

        return left_child if self.heap[left_child] < self.heap[right_child] else right_child

    def _swap(self, i, j):
        aux = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = aux

    def _heapify_up(self, i):
        while self.heap[i] < self.heap[self._father(i)]:
            j = self._father(i)
            self._swap(i, j)
            i = j

    def _heapify_down(self, i):
        while self.heap[i] > self.heap[self._min_child(i)]:
            j = self._min_child(i)
            self._swap(i, j)
            i = j

    def insert_key(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def change_key(self, i, key):
        self.heap[i] = key
        self._heapify_up(i)

    def extract_min(self):
        min = self.heap[0]
        self.heap[0] = float('inf')

        i = self._heapify_down(0)
        self.heap.pop(i)

        return min


if __name__ == '__main__':
    heap = Heap()
    heap.insert_key(5)
    heap.insert_key(4)
    heap.insert_key(9)
    heap.insert_key(2)
    heap.insert_key(13)
    heap.extract_min()
