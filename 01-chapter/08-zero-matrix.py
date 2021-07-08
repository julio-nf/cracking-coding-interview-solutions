def nullify_row(row: int, mtx: list[list[int]]) -> list[list[int]]:
    mtx[row] = [0] * len(mtx[0])

    return mtx


def nullify_col(col: int, mtx2: list[list[int]]) -> list[list[int]]:
    for row in mtx2:
        row[col] = 0

    return mtx2


def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    row = 0
    col = 0
    zeroed_matrix = list(map(list, matrix))

    while row < len(matrix):
        col = 0
        while col < len(matrix[row]):
            if matrix[row][col] == 0:
                zeroed_matrix = nullify_row(row, zeroed_matrix)
                zeroed_matrix = nullify_col(col, zeroed_matrix)
                break
            col += 1
        row += 1

    return zeroed_matrix


if __name__ == '__main__':
    print(zero_matrix(
        [
            [1, 2, 0, 3],
            [0, 4, 1, 7],
            [2, 1, 3, 8],
            [9, 0, 5, 2],
        ]
    ))

# [0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 8],
# [0, 0, 0, 0],
