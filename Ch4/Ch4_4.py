n = int(input())
if 1 <= n <= 10000:
    _sum = 0
    for i in range(1, n+1):
        _sum += i
    print(_sum)
else:
    print("n은 1과 10000사이어야 합니다. ")