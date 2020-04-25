t = int(input())

for i in range (t):
    pow = 2048
    menu = 0
    n = int(input())
    while n != 0:
        menu += int(n / pow)
        n = n % pow
        pow /= 2
    print(menu)