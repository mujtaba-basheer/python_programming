def sml (n):
    curr = [100, 50, 10, 5, 2, 1]
    c, i = 0, 0
    while n !=0:
        c += int(n / curr[i])
        n = n % curr[i]
        i += 1
    return c

t = int(input())

for i in range (t):
    val = int(input())
    print(sml(val))