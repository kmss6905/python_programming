def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def f2(num):
    a = str(num).strip("0")
    return a[-5:]

num = int(input())
print(f2(factorial(num)))
