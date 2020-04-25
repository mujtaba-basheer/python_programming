t = int(input())

for i in range (t):
    s, w1, w2, w3 = map(int, input().split())
    arr = [w1, w2, w3]
    
    if arr[0] + arr[1] + arr[2] <= s:
        print(3)
    elif arr[0] + arr[1] <= s:
        print(2)
    elif arr[1] + arr[2] <= s:
        print(2)
    else:
        print(3)