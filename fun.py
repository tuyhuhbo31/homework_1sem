# factorial f(n) = n*f(n-1)
# f(1) = 1
def fact(x):
    if x == 1:
        return 1
    return x*fact(x-1)
print(fact(5))

def fact_it(x):
    res = 1
    for i in range(2,x+1):
        res *= i
    return res
print(fact_it(5))


#fin f(n) = f(n-1) + f(n-2)
#f(0) = 0, f(1) = 1

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

#cache = [n] = f(n) - список
def fib_memo(n, cache = []):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if cache[n] != 0:
        return cache[n]
    cache[n] = fib_memo(n-1,cache)+fib_memo(n-2,cache)
    return cache[n]


import time
t = time.time()
cache = [0]*51
print(fib_memo(50,cache))
t = time.time() - t
print(t)



