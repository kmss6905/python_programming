a, b = input().split()
if 1 <= int(a) < 20 and 10 <= int(b) < 30:
    if a >= b:
        print('첫번 쨰 수는 두번 쨰 수보다 작아야합니다.', ' 프로그램 종료')
        exit(0)
    else:
        _list = [2**i for i in range(int(a), int(b) + 1) if i != int(a)+1 and i != int(b) - 1]
        print(_list)
