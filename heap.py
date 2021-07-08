class Heap():
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [float('inf')] * max_size

    def _father(self, i):
        return 0 if i == 0 else (i - 1) // 2

    def _left_child(self, i):
        return (2 * i) + 1

    def _right_child(self, i):
        return (2 * i) + 2

    def _min_child(self, i):
        left_child = self._left_child(i)
        right_child = self._right_child(i)

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
        if self.size + 1 > self.max_size:
            return None

        self.heap[self.size] = key
        self.size += 1

        self._heapify_up(self.size - 1)

    def change_key(self, current_key, changed_key):
        index = self.heap.index(current_key)
        self.heap[index] = changed_key
        self._heapify_up(index)

    def extract_min(self):
        min = self.heap[0]
        self.heap[0] = float('inf')

        self._heapify_down(0)

        return min


if __name__ == '__main__':
    heap = Heap(10)
    heap.insert_key(5)
    heap.insert_key(4)
    heap.insert_key(9)
    heap.insert_key(2)
    heap.insert_key(13)
    heap.extract_min()
    heap.change_key(13, 3)
    heap.insert_key(6)
