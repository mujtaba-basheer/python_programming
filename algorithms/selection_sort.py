n = int(input())

arr = list(map(int, input().split()))
min_index = 0

for i in range(1, n):

    j = i - 1
    while(arr[j] > arr[i] and j >= 0):
        j -= 1
    min_index = j
    
    for j in range(i, min_index + 1, -1):
        temp = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = temp

for i in range(n):
    print(arr[i], end = " ")
print()