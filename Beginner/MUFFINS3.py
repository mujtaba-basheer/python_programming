t = int(input())

for i in range (t):
    n = int(input())
    if n % 2 == 1:
        n -= 1
    print(int(n / 2 + 1))