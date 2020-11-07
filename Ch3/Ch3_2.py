
# 문자열 반복
# 2번

number = int(input())
lists = []
for i in range(number):  # 2
    lists.append(input())

for ns in lists:
    num = int(ns[0])
    string = ns[2:]

    for s in string:
        print(s * num, end="")
    print()
