# Three stacks in a array can be implemented in several ways:
# 1 - We can set a fixed size for each stack, such that every stack should
#    occupy a maximum of 1/3 of the array size. This is not a good
#    implementation if some stacks needs to be bigger than others
# 2 - To do it dinamically we need to keep track of how many elements there is
#    in every stack or hold the index of where every stack begins, so we can
#    check if there is enough space for new elements

# Here is an implementation of a three-in-one stack using dyinamic allocation:
class ThreeStackDynamic():
    def __init__(self):
        self.array = [None, None, None]
        self.first_index = 0
        self.second_index = 1
        self.third_index = 2
        self._update_mapper()

    def _update_mapper(self):
        self.mapper = {
            1: self.first_index,
            2: self.second_index,
            3: self.third_index
        }

    def _update_pointers(self, stack: int, operation: str):
        if operation == self.push.__name__:
            if stack != 3:
                if stack == 1:
                    self.second_index += 1
                self.third_index += 1
        else:
            if stack != 3:
                if stack == 1:
                    self.second_index -= 1
                self.third_index -= 1

        self._update_mapper()

    def push(self, value: int, stack: int):
        index = self.mapper[stack]

        if self.array[index] is None:
            self.array[index] = value
        else:
            self.array.insert(index, value)
            self._update_pointers(stack, self.push.__name__)

    def pop(self, stack: int):
        index = self.mapper[stack]

        if self.array[index] is None:
            return None
        else:
            #  1  2     3
            # [1, 9, 2, 8, 3]
            self._update_pointers(stack, self.pop.__name__)
            return self.array.pop(index)


if __name__ == '__main__':
    three_stack = ThreeStackDynamic()
    three_stack.push(1, 1)
    three_stack.push(2, 2)
    three_stack.push(3, 3)
    three_stack.push(7, 1)
    three_stack.push(8, 3)
    three_stack.push(9, 2)
    three_stack.pop(1)
    three_stack.pop(3)
    three_stack.pop(2)
