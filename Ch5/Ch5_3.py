# f(1) = 1 1항 1
# f(2) = 1  2항 1
# f(3) = f(1) + f(2)

def fibo(n):
    a, b = 1, 1
    _list = [a, b]
    for i in range(n-2):
        c = a+b
        _list.append(c)
        a=b
        b=c
    return _list[len(_list) - 1]

num = int(input("정수를 입력하세요 : "))
print(fibo(num))


