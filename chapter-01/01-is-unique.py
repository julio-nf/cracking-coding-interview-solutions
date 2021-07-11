heap = {}


def check_if_exists(char: str) -> bool:
    if char in heap:
        return False

    heap[char] = 1
    return True


def is_unique(string: str) -> bool:
    for char in string:
        if not check_if_exists(char):
            return False

    return True


if __name__ == '__main__':
    print(is_unique('abcd'))
