# code to find peak of a 2D matrix

# taking input of no. of rows and columns
r, c = map(int, input().split())
arr = [[] for i in range(r)]

for i in range(r):
    arr[i] = list(map(int, input().split()))

c_init = 0
c_lim = c - 1
r_init = 0
r_lim = r - 1
is_found = False

while r_init <= r_lim and c_init <= c_lim:

    r_index = int((r_init + r_lim) / 2)
    max_index = c_init

    # finding the global maximum in the row
    for i in range(c_init, c_lim + 1):
        if arr[r_index][i] > arr[r_index][max_index]:
            max_index = i

    # comparing with upper and lower neighbours
    if r_index != 0 and arr[r_index][max_index] < arr[r_index - 1][max_index]:
        r_lim = r_index - 1
    elif r_index != r - 1 and arr[r_index][max_index] < arr[r_index + 1][max_index]:
        r_init = r_index + 1
    else:
        print(f"peak is {arr[r_index][max_index]}, found at ({r_index}, {max_index})")
        is_found = True
        break

    c_index = int((c_init + c_lim) / 2)
    max_index = r_init

    # finding the global maximum in the column
    for i in range(r_init, r_lim + 1):
        if arr[i][c_index] > arr[max_index][c_index]:
            max_index = i

    # comparing with left and right neighbours
    if c_index != 0 and arr[max_index][c_index] < arr[max_index][c_index - 1]:
        c_lim = c_index - 1
    elif c_index != c - 1 and arr[max_index][c_index] < arr[max_index][c_index + 1]:
        c_init = c_index + 1
    else:
        print(f"peak is {arr[max_index][c_index]}, found at ({max_index}, {c_index})")
        is_found = True
        break

if is_found == False:
    print("no peak found")