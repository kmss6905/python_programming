n = int(input())

strings = []

for _ in range(n):
    strings.append(input())

for s in strings:
    num = int(s[0])
    string = s[2:]

    for ss in string:
        print(ss * num, end="")

    print()