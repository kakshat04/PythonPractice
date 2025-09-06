class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        return self.name

    def years(self):
        return self.age

class B(A):
    def __init__(self, name, age):
        A.__init__(self, name, age)

    def fullname(self, lastname):
        return self.name + " " + lastname

    def years(self):
        old_age = super().years()
        return old_age + self.age

b = B("John", 35)
print(b.fullname("John"))
print(b.years())
