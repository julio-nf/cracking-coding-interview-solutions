class Node():
    def __init__(self, value: tuple[int], next=None) -> None:
        self.next = next
        self.value = value


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append_to_tail(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def peek_head(self) -> int:
        if self.head is not None:
            return self.head.value

    def remove_head(self) -> None:
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next
            return value


class AnimalShelter():
    def __init__(self):
        self.dog_list = LinkedList()
        self.cat_list = LinkedList()
        self.animal_type = {
            'cat': self.cat_list,
            'dog': self.dog_list
        }
        self.animal_counter = 0

    def enqueue(self, animal: str) -> None:
        self.animal_counter += 1
        self.animal_type[animal].append_to_tail((animal, self.animal_counter))

    def dequeue_any(self) -> str:
        (_, dog_age) = self.dog_list.peek_head()
        (_, cat_age) = self.cat_list.peek_head()

        if dog_age is not None or cat_age is not None:
            self.animal_counter -= 1
            return self.dog_list.remove_head() \
                if dog_age is not None and dog_age < cat_age \
                else self.cat_list.remove_head()

    def dequeue_dog(self) -> str:
        dog = self.dog_list.remove_head()

        if dog is not None:
            self.animal_counter -= 1
            return dog

    def dequeue_cat(self) -> str:
        cat = self.cat_list.remove_head()

        if cat is not None:
            self.animal_counter -= 1
            return cat


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    animal = shelter.dequeue_any()
    dog = shelter.dequeue_dog()
    cat_any = shelter.dequeue_any()
    cat = shelter.dequeue_cat()
    cat = shelter.dequeue_cat()
    dog = shelter.dequeue_dog()
    dog = shelter.dequeue_dog()
