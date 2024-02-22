class MyNumbers:
  def __iter__(self):
    self.san = 4
    return self

  def __next__(self):
    if self.san <= 20:
      x = self.san
      self.san += 6
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)