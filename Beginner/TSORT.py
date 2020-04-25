t = int(input())
arr = list()
for i in range (t):
    n = int(input())
    arr.append(n)
    
for i in range (t - 1):
    for j in range (i + 1, t):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in range (t):
    print(arr[i])