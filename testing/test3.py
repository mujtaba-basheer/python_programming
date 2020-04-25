import math

a, b = map(int, input().split())

t = math.gcd(a, b)
c = 1
flag = True

if a == b:
    flag = False
    d = int(a / 2)
    for i in range(1, d + 1):
        if a % i == 0:
            c += 1

while t != 1 and flag:
    c += 1
    a = int(a / t)
    b = int(b / t)
    t = math.gcd(a, b)

print(c)