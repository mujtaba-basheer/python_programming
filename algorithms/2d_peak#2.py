# code to find peak of a 2D matrix

# taking input of no. of rows and columns
r, c = map(int, input().split())

arr = [[] for i in range(r)]

for i in range(r):
    arr[i] = list(map(int, input().split()))

r_index = 0
c_index = 0
is_found = False

while r_index < r or c_index < c:

    # checking upper element
    if r_index != 0 and arr[r_index][c_index] < arr[r_index - 1][c_index]:
        r_index -= 1

    # checking lower element
    elif r_index != r - 1 and arr[r_index][c_index] < arr[r_index + 1][c_index]:
        r_index += 1

    # checking element to the left
    elif c_index != 0 and arr[r_index][c_index] < arr[r_index][c_index - 1]:
        c_index -= 1

    # checking element to the right
    elif c_index != c - 1 and arr[r_index][c_index] < arr[r_index][c_index + 1]:
        c_index += 1

    # peak found!
    else:
        print(f"peak is {arr[r_index][c_index]}, found at ({r_index}, {c_index})")
        is_found = True
        break

if is_found == False:
    print("peak not found")