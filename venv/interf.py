from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def details(self):
        print("Inside Interface Method 1")

    @abstractmethod
    def details2(self, test):
        print(f"Inside Interface Method 2 for {test}")

class B(A):
    def details(self):
        print("This is detail")

    def details2(self, test):
        super().details2(test)
        print(f"This is detail2 for {test}")


obj = B()
obj.details()
obj.details2(10)
