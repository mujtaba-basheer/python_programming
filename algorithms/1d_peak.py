a = list(map(int, input().split()))

init = 0
lim = len(a) - 1
is_found = False

while init <= lim:
    index = int((init + lim) / 2)
    # print(f"checking at index {index}")
    if index != 0 and a[index] < a[index - 1]:
        lim = index - 1
    elif index != len(a) - 1 and a[index] < a[index + 1]:
        init = index + 1
    else:
        print(f"peak found at index {index}")
        init = lim + 1
        is_found = True

if is_found == False:
    print("peak not found")