# Duck Typing
class A:
    def a1(self):
        print("A1")

class B:
    def a1(self):
        print("A2.1")

def check(data):
    print(data.a1())

# a1 = A()
# b1 = B()
# check(a1)
# check(b1)

# Method Overriding
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("in base class method")
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def details(self):
        super().details()
        print(self.id)

x = Student("abc", 27, 10)
x.details()


# Method Overloading
def addnums(*nums):
    return sum(nums)
print(addnums(1, 2, 3))
print(addnums(1, 2))
print(addnums(1, 2, 3))

def fun(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

fun(a=10, b=20, c=30)

