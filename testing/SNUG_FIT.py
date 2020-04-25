t = int(input())
a = list()
b = list()

for i in range (t):
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    sum = 0

    for j in range (n):
        sum += min(a[j], b[j])

    print(sum)