t = int(input())

for i in range (t):
    a, b = map(int, input().split())
    max = a + b
    if a > b:
        min = a
    else:
        min = b
    print(min, max)