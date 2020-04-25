def calc (s):
    sum = 0
    for i in range (len(s)):
        sum += int(s[i])
    return sum

t = int(input())
for i in range (t):
    n = str(input())
    print(calc(n))