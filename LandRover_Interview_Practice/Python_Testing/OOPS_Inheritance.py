class Rover:
    def greet(self):
        print("Hello World")

class Range(Rover):
    def greet(self):
        super().greet()

class LandRover(Range, Rover):
    def check1(self):
        super().greet()

obj = LandRover()
obj.check1()
