def calc4 (n):
    c = 0
    for i in range (len(n)):
        if n[i] == '4':
            c += 1
    return c

t = int(input())

for i in range (t):
    num = input()
    print(calc4(num))