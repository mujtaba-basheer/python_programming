import time

n = int(input())
memo = dict()

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def fibo_using_dp(n):
    global memo
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            a = fibo_using_dp(n - 1) + fibo_using_dp(n - 2)
            memo[n] = a
            return a

t1 = time.time()
f = fibo(n)
t2 = time.time()
print(f, "time taken using naive recursion ->", (t2 - t1), "secs")

t1 = time.time()
f = fibo_using_dp(n)
t2 = time.time()
print(f, "time taken using dynamic programming ->", (t2 - t1), "secs")