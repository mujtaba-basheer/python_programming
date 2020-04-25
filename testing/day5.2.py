n = int(input())

limit = int(n / 2)

for i in range (n):
    for j in range (n):
        if((abs(j - i) >= limit) or (i + j <= limit)):
            print("*", end="")
        else:
            print(" ", end="")
    print("")