def FL (n):
    sum = int(str(n)[0]) + n % 10
    return sum

t = int(input())
for i in range (t):
    n = int(input())
    print(FL(n))