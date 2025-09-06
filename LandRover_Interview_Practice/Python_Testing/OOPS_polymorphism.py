"""
Polymorphism are of 4 types:
1. Duck Typing
2. Method Overloading
3. Method Overriding
4. Operator Overloading
"""

from abc import ABC, abstractmethod
# Duck Typing
class Duck:
    def sound(self):
        return "Duck sound"

class AnotherBird:
    def sound(self):
        return "Another Bird, similar sound"

def make_sound(duck):
    return duck.sound()

duck = Duck()
another_bird = AnotherBird()
print(make_sound(duck))
print(make_sound(another_bird))

# Method Overriding
class A(ABC):
    @staticmethod
    def method1(): ...

class B(A):
    def method1(self):
        super().method1()
        print("Inside B")
        return

class C(A):
    def method1(self):
        super().method1()
        print("Inside C")
        return

shape = B()
shape.method1()

# Method Overloading : Python does not allow overloading methods by default, but that can be done using *
class A1:
    def method1(self, *a:int):
        print(f"Inside A1 : {a}")

obj = A1()
obj.method1(10, 10)

# Operator Overloading
class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

a = A(1)
b = A(2)
print(a+b)

class Dog:
    def __init__(self, age):
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age




