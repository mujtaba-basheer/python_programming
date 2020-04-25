def fctrl (n):
    f = 1
    for i in range (1, n + 1):
        f *= i
    return f

t = int(input())

for i in range (t):
    n = int(input())
    print(fctrl(n))