from collections import deque


def operation():
    for op in a:
        if op[0] not in operation_list:
            exit(0)
        else:
            if op[0] == push:
                deque_list.append(int(op[1]))
            if op[0] == front:
                if len(deque_list) != 0:
                    print(deque_list[0])
                else:
                    print(-1)
            if op[0] == back:
                if len(deque_list) != 0:
                    print(deque_list[len(deque_list) - 1])
                else:
                    print(-1)
            if op[0] == empty:
                if len(deque_list) != 0:
                    print(0)
                else:
                    print(1)
            if op[0] == size:
                print(len(deque_list))
            if op[0] == pop:
                if len(deque_list) != 0:
                    print(deque_list.popleft())
                else:
                    print(-1)


if __name__ == "__main__":
    operation_list = push, front, back, size, empty, pop = ['push', 'front', 'back', 'size', 'empty', 'pop']
    num = int(input())
    a = [input().split() for _ in range(num)]
    deque_list = deque()
    operation()
