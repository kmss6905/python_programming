matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
matrix_c = [[1, 4, 2, 6], [2, 5, 7, 8]]
matrix_d = [[1, 2], [3, 4], [5, 6], [9, 1]]

def matrix_mul(*args):
    lists = [*args]
    if len(args) == 1:
        return print(*lists)
    result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*args[1])] for row_a in args[0]]
    lists.pop(1)
    lists[0] = result
    matrix_mul(*lists)

matrix_mul(matrix_a, matrix_b, matrix_c, matrix_d)