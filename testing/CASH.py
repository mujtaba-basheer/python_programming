t = int(input())

for i in range (t):
    n, k = map(int, input().split())

    add = [0 for i in range (n + 1)]
    subtract = [0 for i in range (n + 1)]
    subtract[0] = 0
    add[n] = 0
    ans = k;

    arr = list(map(int, input().split()))

    for j in range (1, n + 1):
        subtract[j] = arr[j - 1] % k
        subtract[j] += subtract[j - 1]

        add[j - 1] = (k - (arr[j - 1] % k)) % k

    for j in range (n, 0, -1):
        add[j - 1] += add[j]
        if subtract[j] >= add[j]:
            if subtract[j] - add[j] < ans:
                ans = subtract[j] - add[j]
        else:
            break

    print(ans)