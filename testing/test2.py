def getMax(perm = [], amt = 0, maxShow = 0, loop = 1):
    for i in range(4):
        if i in perm == False:
            perm.append(i)
            getMax(perm, amt, maxShow, loop + 1)
            perm.pop()

    if(len(perm) == 4):
        shows = []
        for j in range(4):
            shows[j] = arr[perm[j]]
        shows.sort()

        j = 4;
        for x in sortedArr:
            if x == 0:
                amt -= 100
            else:
                amt += (j * 25 * arr[i])
            j -= 1

        if amt > maxShow:
            maxShow = amt
            cost = maxShow

        if loop == 24:
            return amt

        return 0

t = int(input())
totalCost = 0

for i in range (t):
    n = int(input())

    cost = 0
    arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for j in range(n):
        m, time = map(str, input().split())

        m = m.split()[0]
        time = int(time)

        time = int((time / 3) % 4)
        show = int(ord(m) - 65)

        arr[show][time] += 1

    cost = getMax()
    
    totalCost += cost

    print(cost)

print(totalCost)
