def flatten(data):
    _list = []
    for i in data:
        if type(i) == list:
            for j in i:
                _list.append(j)
        else:
            _list.append(i)
    return _list


example = [[1,2,3], [4,5,6], 7, [8,9]]
print("원본:", example)
print("변환:", flatten(example))