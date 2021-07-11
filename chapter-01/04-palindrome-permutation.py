# Tacat Coa
# aaaccott

# Tacao Cat
# taco cat, atco cta


def count_characters(string: str) -> dict[str, int]:
    counter = {}

    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter


def check_palindrome_permutation(string: str) -> bool:
    char_counter = count_characters(string.replace(' ', '').lower())
    odd_counter = 0

    for char in char_counter:
        if char_counter[char] % 2 != 0:
            if odd_counter >= 1:
                return False
            odd_counter += 1

    return True


if __name__ == '__main__':
    print(check_palindrome_permutation('Tact Coa'))
