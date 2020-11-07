_list = a, b, c = list(map(int, input().split()))
for i in _list:
    if i < 1 or i > 100:
        print("모든 입력 값은 1이상 100이하의 값이어야만 합니다.")
        exit()
for i in range(1, len(_list)):
    for j in range(i, 0, -1):
        if _list[j] < _list[j - 1]:
            _list[j], _list[j - 1] = _list[j - 1], _list[j]
        else:
            break
print(_list[1])



