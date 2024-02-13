"""
Вы можете указать, что функция может иметь ТОЛЬКО позиционные аргументы или ТОЛЬКО аргументы в виде ключевых слов.

Чтобы указать, что функция может иметь только позиционные аргументы, добавьте , / после аргументов:

"""
def my_function(x, /):
  print(x)

my_function(3)

# Без , / разрешается использовать аргументы в виде ключевых слов, даже если функция ожидает позиционные аргументы:

def my_function(x):
  print(x)

my_function(x = 3)

# Код снизу выдаст ошибку если мы одновременно проинициализируем переменную при вызове функции и внутри функции добавим , /

def my_function(x, /):
  print(x)

my_function(x = 3)
