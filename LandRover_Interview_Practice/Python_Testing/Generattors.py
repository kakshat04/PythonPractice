def gen(n:int):
    for i in range(n):
        yield i

counter = gen(10)
for i in counter:
    print(i)


x = (i*i for i in range(10))
print([i for i in x])

# fibonacci using generators
def fib(n:int):
    fibo = []
    a, b = 0, 1
    while True:
        c = a + b
        if c>n:
            break
        # fibo.append(c)
        yield c
        a, b = b, c
    return fibo

print(fib(10))
for i in fib(10):
    print(i)