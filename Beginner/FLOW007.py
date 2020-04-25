def rev (n):
    revNo = 0
    for i in range (len(n)):
        revNo += int(n[i]) * 10 ** i
    return revNo

t = int(input())

for i in range (t):
    num = input()
    print(rev(num))