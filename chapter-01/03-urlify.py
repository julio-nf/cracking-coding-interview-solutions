# O(n²) since string slicing is O(n)
def urlify(string: str) -> str:
    def replace_slice_url(string: str, i: int, j: int) -> str:
        return string[:i] + "%20" + string[j:]

    string = string.strip()
    i = len(string) - 1
    j = i
    while i != 0:
        if string[i] == ' ':
            while string[j] == ' ':
                j -= 1
            string = replace_slice_url(string, j + 1, i + 1)
            i = j
        else:
            i -= 1
            j = i

    return string


if __name__ == '__main__':
    print(urlify('Ola,  tudo      bem    '))
    print(urlify('Mr John Smith    '))
