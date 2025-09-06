"""
astraction - to make sure all functions in a class are used by child class
used as in interface
"""
from abc import ABC, abstractmethod

class Rover(ABC):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    @abstractmethod
    def move(self):
        return self.x + self.y

    @abstractmethod
    def land(self):
        return self.x - self.y

class LandRover(Rover):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def move(self):
        return super().move()

    def land(self):
        return super().land()

obj = LandRover(20, 10)
print(obj.land())
print(obj.move())


