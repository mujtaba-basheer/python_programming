t = int(input())

for i in range(t):
    n, p = map(int, input().split())
    d = list(map(int, input().split()))

    ans = [0 for j in range(n)]
    amount = 0
    index = n - 1

    while True:
        rem = p - amount
        if rem % d[index] == 0:
            if index == 0:
                flag = False
                break

            amount += (int(rem / d[index] - 1) * d[index])
            ans[index] += int(rem / d[index] - 1)
            index -= 1

        else:
            flag = True
            ans[index] += int(rem / d[index] + 1)
            break

    if flag == False:
        print("NO")
    else:
        print("YES", end = " ")
        for j in range(n):
            print(ans[j], end = " ")

    print()