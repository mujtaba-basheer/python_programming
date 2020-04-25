n = int(input())

arr = list(map(int, input().split()))
min_index = 0

for i in range(1, n):

    init = 0
    lim = i - 1
    min_index = i - 1

    while init <= lim:
        mid = int((init + lim) / 2)
        if mid == 0 and arr[mid] > arr[i]:
            min_index = -1
            break
        elif arr[mid] <= arr[i] and arr[mid + 1] >= arr[i]:
            min_index = mid
            break
        else:
            lim = mid - 1
    
    for j in range(i, min_index + 1, -1):
        temp = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = temp

for i in range(n):
    print(arr[i], end = " ")
print()