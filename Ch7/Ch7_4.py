def check_land_mine(m: list, x: int, y: int):
    """
    m(x,y) 주변에 있는 지뢰의 개수를 리턴합니다.

    :param m: 지뢰개수를 구하기 위한 타켓팅 되는 메트릭스
    :param x: 좌표
    :param y: 좌표
    :return: num : m(x,y) 주변에 있는 지뢰의 개수
    """
    num = 0
    # 왼쪽
    if y >= 1:
        if m[x][y - 1] == '*':
            num += 1
            # print("왼쪽")

    # 오른쪽
    if y < _y - 1:
        if m[x][y + 1] == '*':
            num += 1
            # print("오른쪽")

    # 위
    if x >= 1:
        if m[x - 1][y] == '*':
            num += 1
            # print("위")

    # 아래
    if x != _x - 1:
        if m[x + 1][y] == '*':
            num += 1
            # print("아래")

    # 좌측상단대각선
    if x >= 1 and y >= 1:
        if m[x - 1][y - 1] == '*':
            num += 1
            # print("좌측상단")

    # 좌측하단대각선
    if x < _x - 1 and y >= 1:
        if m[x + 1][y - 1] == '*':
            num += 1
            # print("좌측하단")

    # 우측상단대각선
    if x >= 1 and y < _y - 1:
        if m[x - 1][y + 1] == '*':
            num += 1
            # print("우측상단")

    # 우측하단
    if x != _x - 1 and y < _y - 1:
        if m[x + 1][y + 1] == '*':
            num += 1
            # print("우측하단")

    return num


def change_matrix(m: list):
    """
    바뀐 결과 메트릭스(리스트)를 출력함

    :param m:
    :return:
    """
    for i in range(_x):
        for j in range(_y):
            if m[i][j] == ".":
                m[i][j] = check_land_mine(m, i, j)
    return m


def print_matrix(m: list):
    """
    매트릭스(리스트)를 출력하는 함수

    :param m:
    :return: 각 행들을 출력합니다
    """
    for i in range(_x):
        row = ""
        for j in range(_y):
            row += str(m[i][j])
        print(row)


if __name__ == '__main__':
    _x, _y = map(int, input().split())  # 사용자로 부터 메트릭스 크기 입력 받음
    matrix = [list(input()) for _ in range(_y)]  # 크기에 맞게 메트릭스에 값을 채움
    print_matrix(change_matrix(matrix))  # 바뀐 메트릭스 출력
