from functools import reduce
a = int(input())
if 10 <= a <= 50:
    number = format(reduce(lambda x, y: x*y, [i+1 for i in range(a)]), ',')
    print(number)
else:
    print('a는 10이상 50이하')