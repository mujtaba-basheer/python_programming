# heapify function

def max_heapify(arr = list(), i = 0):
    ind = i * 2 + 1
    n = len(arr)
    while ind < n and arr[i] <= arr[ind] or ind + 1 < n and arr[i] <= arr[ind + 1]:
        max_ind = ind + 1 if ind + 1 < n and arr[ind] < arr[ind + 1] else ind
        # print(f"swapping {arr[i]} and {arr[max_ind]}")
        temp = arr[i]
        arr[i] = arr[max_ind]
        arr[max_ind] = temp
        i = max_ind
        ind = i * 2 + 1
    return arr

# function to return max element in current heap

def extract_max():
    global arr
    n = len(arr)
    i = 0
    if n == 0:
        return None
    temp = arr[i]
    arr[i] = arr[n - 1]
    arr.pop()
    arr = max_heapify(arr, 0)
    return temp

# main implementation

n = int(input())

arr = list(map(int, input().split()))

for i in range(int(n / 2) - 1, -1, -1):
    arr = max_heapify(arr, i)

print("Corresponding Max Heap array:")
for i in range(n):
    print(arr[i], end=" ")
print()

print("Corresponding sorted array, sorted by Heap Sort:")
for i in range(n):
    print(extract_max(), end=" ")
print()