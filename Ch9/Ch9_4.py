import operator


def vector_sub(a, *args):
    result = [sum(t) for t in zip(*args)]
    print(list(map(operator.sub, a, result)))


vector_sub([1, 3], [2, 4])
vector_sub([1, 5], [10, 4], [4, 7])
vector_sub([10, 9, 8], [1, 2, 3], [1, 1, 1])