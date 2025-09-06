class A:
    def method(self):
        print("A")

x = A()
x.method()

class B:
    var = 10
x = B()
print(x.var)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def details(self):
        return f"Name is {self.name}, Age is {self.age}"

class Student(Person):
    def __init__(self, gender, color):
        super().__init__("John", 35)
        # Person.__init__(self, "John", 35)
        self.gender = gender
        self.color = color

    def details2(self):
        return f"In Child Class, Gender is {self.gender}, Color is {self.color}, name is {self.name}, Age is {self.age}"


x = Person("Akshat", 37)
y = Student("Male", "Brown")
print(x)
print(y.details())
print(y.details2())
print(y.gender)
print(y.color)

print(x.name)
print(x.age)
print(x.details())


