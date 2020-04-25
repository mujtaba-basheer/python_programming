def merge(a1 = list(), a2 = list()):
    i1 = len(a1) - 1
    i2 = len(a2) - 1
    a = [0 for i in range(len(a1) + len(a2))]

    i = len(a1) + len(a2) - 1
    while i1 > -1 or i2 > -1:
        if i2 == -1 or i1 != -1 and a1[i1] >= a2[i2]:
            a[i] = a1[i1]
            i1 -= 1
        elif i1 == -1 or i2 != -1 and a1[i1] < a2[i2]:
            a[i] = a2[i2]
            i2 -= 1
        i -= 1

    return a

def sort(arr = list()):
    l = len(arr)
    if l == 1:
        return arr
    else:
        a1 = [arr[i] for i in range(int((l - 1) / 2 + 1))]
        a2 = [arr[i] for i in range(int((l - 1) / 2) + 1, l)]
        return merge(sort(a1), sort(a2))

n = int(input())

arr = list(map(int, input().split()))
sorted_arr = sort(arr)

for i in range(n):
    print(sorted_arr[i], end = " ")
print()