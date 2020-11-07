matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
matrix_c = [[1, 4, 2, 6], [2, 5, 7, 8]]
# 첫번 쨰 행렬의 행을 뽑는다.
# 두번 쨰 행렬의 열을 뽑는다.
# result = [[sum(a*b) for a, b in zip(row_a, column_b) for column_b in zip(*matrix_b)] for row_a in matrix_a]
# print(result)

# for row_a in matrix_a:
#     for column_b in zip(*matrix_b):
#         print(row_a, column_b)
#         for a, b in zip(row_a, column_b):
#             print(a, b, a * b)

result = []
for row_a in matrix_a:
    row_v = []
    for column_b in zip(*matrix_b):
        print(row_a, column_b)
        dot_product = 0
        for r_a, c_b in zip(row_a, column_b):
            dot_product += r_a * c_b
        row_v.append(dot_product)
    result.append(row_v)

print(result)






