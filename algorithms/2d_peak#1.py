# code to find peak of a 2D matrix

# taking input of no. of rows and columns
r, c = map(int, input().split())
arr = [[] for i in range(r)]

for i in range(r):
    arr[i] = list(map(int, input().split()))

init = 0
lim = c - 1
is_found = False

while init <= lim:
    index = int((init + lim) / 2)
    max_index = 0

    # finding the global maximum
    for i in range(r):
        if arr[i][index] > arr[max_index][index]:
            max_index = i

    # checking for peak
    if index != 0 and arr[max_index][index] < arr[max_index][index - 1]:
        lim = index - 1
    elif index != c - 1 and arr[max_index][index] < arr[max_index][index + 1]:
        init = index + 1
    else:
        print(f"peak is {arr[max_index][index]}, found at ({max_index}, {index})")
        is_found = True
        break

if is_found == False:
    print("no peak found")