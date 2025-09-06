# z = iter(range(5))
# print(z.__next__())
# print(next(z))

class checkIter:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 5:
            self.count += 1
            return self.count
        else:
            raise StopIteration

values = checkIter()

for value in values:
    print(value)


def fibo_withoutGen(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        print(a, b)

fibo_withoutGen(10)

def decorator(func):
    def wrapper():
        print("aS")
        func()
        print("bS")
    return wrapper

@decorator
def check():
    print("gellp")

check()

def decorator(func):
    def wrapper(*args, **kwargs):
        print("aS")
        func(*args, **kwargs)
        print("bS")
    return wrapper

@decorator
def check2(name):
    print(name)

check2("<UNK>")


def log(func):
    def wrapper(*args, **kwargs):
        print(f"log from file {func.__name__}")
        func(*args, **kwargs)
    return wrapper


@log
def file1():
    print("file1")

file1()

with open("file1.txt", "r") as f:
    f.read()