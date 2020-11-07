# 0 0 이 들어오면 종료
_list = []
while 1:
    a, b = input().split()
    if int(a) == 0 and int(b) == 0:  # 입력값으로 0 0 이 들어올 경우 종료
        for i in _list:
            print(int(i[0]) + int(i[1]))  # list 안의 모든 값을 반복하면서 출력
        break
    _list.append([a, b])




