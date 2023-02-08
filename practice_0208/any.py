def f(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

m = int(input('???'))
print(f(m))
print(f(m)*2+ f(5))
