t = int(input())

for i in range (t):
    a, b = map(int, input().split())
    sign = ""
    if a > b:
        sign = ">"
    elif a < b:
        sign = "<"
    else:
        sign = "="
        
    print(sign)