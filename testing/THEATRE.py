def perm(length, permArr):
    if len(permArr) == length:
        newArr = [0, 0, 0, 0]
        cost = 0
        emptyShows = 0
        global maxCost
        global arr
        for j in range(length):
            newArr[j] = arr[j][permArr[j]]
            if newArr[j] == 0:
                emptyShows += 1
        newArr.sort()
        for j in range(length):
            cost += (newArr[j] * 25 * (1 + j))
        
        cost -= (emptyShows * 100)
        if cost > maxCost:
            maxCost = cost
        return
    else:
        for i in range (length):
            if (i in permArr) == False:
                permArr.append(i)
                perm(length, permArr)
                permArr.pop()

t = int(input())
totalCost = 0

for i in range (t):
    n = int(input())

    maxCost = -400
    arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for j in range(n):
        m, time = map(str, input().split())

        m = m.split()[0]
        time = int(time)

        time = int((time / 3) % 4)
        show = int(ord(m) - 65)

        arr[show][time] += 1

    emptyArr = list()
    perm(4, emptyArr)

    print(maxCost)
    
    totalCost += maxCost

print(totalCost)
