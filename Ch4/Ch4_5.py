n = int(input())
while 1 <= n <= 100:
    for i in range(n + 1):
        print(' ' * (n - i), '*' * i)
    n = int(input())

print("종료. 1과 100사이의 수를 입력하세요.")