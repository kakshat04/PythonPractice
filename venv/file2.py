# a = 0
# b = 1
# for i in range(1, 10):
#     c = a + b
#     a = b
#     b = c
#     print(b)

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))


print(list(map(lambda n: n ** 2, range(10))))
print(list(filter(lambda x: x % 2 == 0, range(10))))
from functools import reduce
print(reduce(lambda x, y: x + y, range(10)))