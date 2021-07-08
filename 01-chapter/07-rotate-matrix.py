# Not in-place algorithm:
def get_matrix_column(col: int, matrix: list[list[str]]) -> list[str]:
    return [row[col] for row in matrix]


def rotate_matrix(matrix: list[list[str]]) -> list[list[str]]:
    rotated_matrix = []
    for i in range(len(matrix)):
        rotated_matrix.append(get_matrix_column(i, reversed(matrix)))

    return rotated_matrix

    # 0,0 -> 0,3
    # 0,3 -> 3,3
    # 3,3 -> 3,0
    # 3,0 -> 0,0

    # 0,1 -> 1,3
    # 1,3 -> 3,2
    # 3,2 -> 2,0
    # 2,0 -> 0,1

    # 0,2 -> 2,3
    # 2,3 -> 3,1
    # 3,1 -> 1,0
    # 1,0 -> 0,2

    # 1,1 -> 2,1
    # 1,2 -> 1,1
    # 2,2 -> 1,2
    # 2,1 -> 2,2

    # abcd        miea
    # efgh  -->   njfb
    # ijkl        okgc
    # mnop        plhd


if __name__ == '__main__':
    print(rotate_matrix(
        [
            ['a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h'],
            ['i', 'j', 'k', 'l'],
            ['m', 'n', 'o', 'p'],
        ]
    )
    )
