def myfunc(n):
  return lambda a : a * n # a = 15 n = 2

mydoubler = myfunc(2)

print(mydoubler(15))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(15))
print(mytripler(11))