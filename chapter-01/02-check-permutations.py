def count_characters(string: str) -> dict[str, int]:
    counter = {}

    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter


def check_permutations(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    string1_counter = count_characters(string1)
    string2_counter = count_characters(string2)

    return string1_counter == string2_counter


if __name__ == '__main__':
    print(check_permutations('abcd', 'abcd'))
    print(check_permutations('abbd', 'abcd'))
    print(check_permutations('abdabbde', 'aabbbdde'))
    print(check_permutations('abdabb', 'aabbbdd'))
