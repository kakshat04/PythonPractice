from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def details(self):
        print("Abstract method")

    def details2(self):
        print("Non Abstract method, Base Class")

class HREmployee(Employee):
    def details(self):
        super().details()
        return

    def details2(self):
        print("Inside Child Class of details2")

# e1 = Employee()  Will not work as it is instantiating abstract class directly
# e1.details()
# e1.details2()

hr = HREmployee()
hr.details()
hr.details2()