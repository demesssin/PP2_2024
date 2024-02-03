class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + str(abc.age)) # Без str код будет выводить ошибку

p1 = Person("John", 36)
p1.myfunc()