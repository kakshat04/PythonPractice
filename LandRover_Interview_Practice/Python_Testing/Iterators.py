iterator = iter(range(10))
print(next(iterator))
# for item in iterator:
#     print(item)
print(iterator.__next__())


class Oddnumbers:

   def __init__(self, end_range):
      self.start = -1
      self.end = end_range

   def __iter__(self):
      return self

   def __next__(self):
      for i in range(self.start, self.end):
          yield i

countiter = Oddnumbers(10)
for i in countiter:
    print(i)
