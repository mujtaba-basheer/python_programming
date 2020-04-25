x, y = map(float, input().split())
if x % 5 == 0:
    x += 0.5
    if y < x:
        print(y)
    else:
        print(y - x)
else:
    print(y)