# def count_characters(string: str) -> dict[str, int]:
#     counter = {}

#     for char in string:
#         if char in counter:
#             counter[char] += 1
#         else:
#             counter[char] = 1

#     return counter


def string_compression(string: str) -> str:
    compressed_list = []

    i = 0
    j = i + 1
    while i < len(string):
        while j < len(string) and string[j] == string[i]:
            j += 1

        to_append = string[i] + str(j - i)
        compressed_list.append(to_append)
        i = j

    if len(compressed_list) < len(string):
        return ''.join(compressed_list)

    return string


if __name__ == '__main__':
    print(string_compression('aabcccccaaa'))
