n = int(input())

arr = list(map(int, input().split()))
b = [arr[i] * (i + 1) for i in range(n)]
b.sort()

ans = 0

for i in range(n):
    if (i + 1) >= arr[i]:
        ans += 1

print(ans)