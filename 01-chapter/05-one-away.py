def count_characters(string: str) -> dict[str, int]:
    counter = {}

    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter


def compare_counters(counter1: dict[str, int], counter2: dict[str, int]) -> bool:
    equal_counter = 0

    for _ in counter1.keys() & counter2.keys():
        equal_counter += 1

    return not equal_counter < 3


def check_one_away(string1: str, string2: str) -> bool:
    return len(string1) - len(string2) in (-1, 0, 1) \
        and compare_counters(count_characters(string1), count_characters(string2))


if __name__ == '__main__':
    print(check_one_away('pale', 'ple'))
    print(check_one_away('pale', 'bale'))
    print(check_one_away('pales', 'pale'))
    print(check_one_away('pale', 'bake'))
