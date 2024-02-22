class MyNumbers:
  def __iter__(self):
    self.san = 3
    return self

  def __next__(self):
    x = self.san
    self.san *= 2
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
